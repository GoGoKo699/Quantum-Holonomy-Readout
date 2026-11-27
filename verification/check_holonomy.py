"""Finite verification of the source, receiver and dumbbell examples.

Run with Python 3 and NumPy. The finite graph search tests the trace witnesses;
it does not replace the analytic invariant-span or resource lower bound proofs.
"""

from itertools import product

import numpy as np


X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def dumbbell(a, b, bridge_length):
    """Return two oriented cycles, the joining path and labeled edges."""
    first_cycle = list(range(a))
    bridge = [0, *range(a, a + bridge_length)]
    second_cycle = [bridge[-1], *range(a + bridge_length, a + bridge_length + b - 1)]
    n = a + b + bridge_length - 1
    edges = {}
    for generator, cycle in enumerate((first_cycle, second_cycle), start=1):
        for start, end in zip(cycle[:-1], cycle[1:]):
            edges[start, end] = 0
        edges[cycle[-1], cycle[0]] = generator
    for start, end in zip(bridge[:-1], bridge[1:]):
        edges[start, end] = 0
    return n, edges, first_cycle, second_cycle, bridge


def mixed_walk(first_cycle, second_cycle, bridge):
    """List the vertices of the closed walk, omitting its repeated endpoint."""
    return first_cycle + bridge[:-1] + second_cycle + bridge[:0:-1]


def source_state(n, edges, gates, eps):
    """Assemble the visibility matrix and the independent mixture expression."""
    d = gates[1].shape[0]
    identity = np.eye(d)
    rho = np.eye(n * d, dtype=complex) / (d * n)
    mixture = np.zeros_like(rho)
    degree = np.zeros(n, dtype=int)
    for (u, v), label in edges.items():
        degree[[u, v]] += 1
        unitary = gates[label] if label else identity
        left = slice(u * d, (u + 1) * d)
        right = slice(v * d, (v + 1) * d)
        rho[left, right] = eps * unitary / (d * n)
        rho[right, left] = eps * unitary.conj().T / (d * n)
        branch = np.zeros((n * d, d), dtype=complex)
        branch[left] = unitary / np.sqrt(2)
        branch[right] = identity / np.sqrt(2)
        mixture += (2 * eps / (n * d)) * (branch @ branch.conj().T)
    for v, weight in enumerate((1 - eps * degree) / n):
        block = slice(v * d, (v + 1) * d)
        mixture[block, block] += weight * identity / d
    np.testing.assert_allclose(mixture, rho, atol=1e-15)
    np.testing.assert_allclose(np.trace(rho), 1, atol=1e-15)
    assert 0 < eps < 1 / max(degree)
    assert np.linalg.eigvalsh(rho)[0] > 0
    return rho


def check_local_score(d):
    """Check the signed count on the exactly-one-photon two-bin sector."""
    identity = np.eye(d)
    beamsplitter = np.kron(np.array([[1, 1], [1, -1]]) / np.sqrt(2), identity)
    signed_ports = np.kron(np.diag([1, -1]), identity)
    score = beamsplitter.conj().T @ signed_ports @ beamsplitter
    np.testing.assert_allclose(score, np.kron(X, identity), atol=1e-15)
    np.testing.assert_allclose(score @ score, np.eye(2 * d), atol=1e-15)


def support_layouts(length):
    """Enumerate pair orientations using the physical one-photon-per-bin cut."""
    accepted = []
    for orientation in product((0, 1), repeat=length):
        occupied_slots = {(i - 1 + side) % length for i, side in enumerate(orientation)}
        if len(occupied_slots) == length:
            accepted.append(orientation)
    return accepted


def check_schedule_and_support():
    assignments = 0
    for length in range(3, 17):
        accepted = support_layouts(length)
        assert accepted == [(0,) * length, (1,) * length]
        assignments += 2**length
        folded = list(range(1, length + 1, 2))
        folded += list(range(length - length % 2, 0, -2))
        assert sorted(folded) == list(range(1, length + 1))
        delays = [abs(folded[i - 1] - folded[i]) for i in range(length)]
        assert max(delays) == 2
    return assignments


def compressed_moments(rho, d, walk):
    """Sum polarization matrix elements on the two allowed site layouts."""
    length = len(walk)
    late_sites = np.array(walk)
    early_sites = np.roll(late_sites, -1)
    for mode_sites in (late_sites, early_sites):
        assert np.all(mode_sites != np.roll(mode_sites, -1))
    polarizations = np.array(list(product(range(d), repeat=length)))
    # Swapping both ports of pair i carries its polarization from slot i-1 to i.
    swapped = np.roll(polarizations, 1, axis=1)
    early_rows = d * early_sites + polarizations
    late_columns = d * late_sites + swapped
    off_diagonal = np.prod(rho[early_rows, late_columns], axis=1)
    mean = 2 * np.real(np.sum(off_diagonal))
    second = 0.0
    for sites in (late_sites, early_sites):
        rows = d * sites + polarizations
        second += np.real(np.sum(np.prod(rho[rows, rows], axis=1)))
    return mean, second


def trace_from_blocks(rho, d, walk):
    """Transfer contraction on a fixed path, linear in its length."""
    matrix = np.eye(d, dtype=complex)
    for start, end in zip(walk, walk[1:] + walk[:1]):
        left = slice(start * d, (start + 1) * d)
        right = slice(end * d, (end + 1) * d)
        matrix = matrix @ rho[left, right]
    return np.trace(matrix)


def rotated_source(rho, d, n, rng):
    frames = np.zeros_like(rho)
    for v in range(n):
        block = slice(v * d, (v + 1) * d)
        draw = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        q, r = np.linalg.qr(draw)
        frames[block, block] = q @ np.diag(np.diag(r) / abs(np.diag(r)))
    return frames @ rho @ frames.conj().T


def reduced_word(word, label, involutions):
    if not label:
        return word
    if involutions:
        label = abs(label)
        inverse = label
    else:
        inverse = -label
    if word and word[-1] == inverse:
        return word[:-1]
    return word + (label,)


def closed_words(n, edges, maximum_length, involutions=False):
    """Enumerate reachable generator words of closed walks at each length."""
    neighbors = [[] for _ in range(n)]
    for (u, v), label in edges.items():
        neighbors[u].append((v, label))
        neighbors[v].append((u, -label))
    by_length = [set() for _ in range(maximum_length + 1)]
    for start in range(n):
        frontier = {(start, ())}
        by_length[0].add(())
        for length in range(1, maximum_length + 1):
            frontier = {
                (v, reduced_word(word, label, involutions))
                for u, word in frontier
                for v, label in neighbors[u]
            }
            by_length[length].update(word for v, word in frontier if v == start)
    return by_length


def word_trace(word, gates):
    matrix = np.eye(gates[1].shape[0], dtype=complex)
    for label in word:
        gate = gates[abs(label)]
        matrix = matrix @ (gate if label > 0 else gate.conj().T)
    return np.trace(matrix)


def first_difference(by_length, gates_0, gates_1):
    for length, words in enumerate(by_length):
        for word in words:
            if abs(word_trace(word, gates_0) - word_trace(word, gates_1)) > 1e-10:
                return length
    return None


def su2_rotation(axis, angle):
    return np.cos(angle) * np.eye(2) + 1j * np.sin(angle) * axis


def block_diagonal(left, right):
    zeros = np.zeros_like(left)
    return np.block([[left, zeros], [zeros, right]])


def check_su4_examples(tuples, eps):
    a_loop = block_diagonal(Z, -Z)
    b_loop_0 = block_diagonal(Z, Z)
    b_loop_1 = block_diagonal(X, X)
    identity = np.eye(4)
    for gate in (a_loop, b_loop_0, b_loop_1):
        np.testing.assert_allclose(gate.conj().T @ gate, identity)
        np.testing.assert_allclose(gate @ gate, identity)
        np.testing.assert_allclose(np.linalg.det(gate), 1)
        np.testing.assert_allclose(np.linalg.eigvalsh(gate), [-1, -1, 1, 1])
    gates_0 = {1: a_loop, 2: b_loop_0}
    gates_1 = {1: a_loop, 2: b_loop_1}
    for gates, target in [(gates_0, 4), (gates_1, -4)]:
        b_loop = gates[2]
        np.testing.assert_allclose(np.trace(a_loop @ b_loop), 0)
        np.testing.assert_allclose(word_trace((1, 2, 1, 2), gates), target)
        commutator = a_loop @ b_loop - b_loop @ a_loop
        np.testing.assert_allclose(4 - np.linalg.norm(commutator, "fro") ** 2 / 2, target)
    for a, b, ell in tuples:
        n, edges, first, second, bridge = dumbbell(a, b, ell)
        walk = mixed_walk(first, second, bridge) * 2
        length = 2 * (a + b + 2 * ell)
        assert len(walk) == length
        words = closed_words(n, edges, length, involutions=True)
        assert first_difference(words, gates_0, gates_1) == length
        scale = (eps / (4 * n)) ** length
        for gates, target in [(gates_0, 4), (gates_1, -4)]:
            rho = source_state(n, edges, gates, eps)
            np.testing.assert_allclose(trace_from_blocks(rho, 4, walk) / scale, target)


def main():
    eps = 0.2
    check_local_score(2)
    check_local_score(4)
    assignments = check_schedule_and_support()
    tuples = [(3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 4, 1), (4, 4, 2), (4, 5, 3)]
    alpha, beta = 0.61, 0.83
    a_loop = su2_rotation(Z, alpha)
    gates_aligned = {1: a_loop, 2: su2_rotation(Z, beta)}
    gates_orthogonal = {1: a_loop, 2: su2_rotation(X, beta)}
    rng = np.random.default_rng(120)
    for a, b, ell in tuples:
        n, edges, first, second, bridge = dumbbell(a, b, ell)
        walk = mixed_walk(first, second, bridge)
        length = a + b + 2 * ell
        assert len(walk) == length
        words = closed_words(n, edges, length)
        assert first_difference(words, gates_aligned, gates_orthogonal) == length
        scale = (eps / (2 * n)) ** length
        for gates, eta in [(gates_aligned, 1), (gates_orthogonal, 0)]:
            rho = source_state(n, edges, gates, eps)
            trace = 2 * (np.cos(alpha) * np.cos(beta) - eta * np.sin(alpha) * np.sin(beta))
            for state in (rho, rotated_source(rho, 2, n, rng)):
                np.testing.assert_allclose(trace_from_blocks(state, 2, walk) / scale, trace)
                if length <= 8:
                    mean, second_moment = compressed_moments(state, 2, walk)
                    np.testing.assert_allclose(mean / scale, 2 * trace)
                    np.testing.assert_allclose(second_moment / (2 * n ** (-length)), 1)
    check_su4_examples(tuples, eps)
    print(f"Physical score support and two-spacing schedule checked for {assignments:,} orientations.")
    print("SU(2) source, gauge invariance and first trace difference checked on six graphs.")
    print("Compressed first and second receiver moments checked on six- and eight-step walks.")
    print("SU(4) commutator example and first trace difference at twice the length checked on six graphs.")


if __name__ == "__main__":
    main()
