# The exact copy threshold

Consider two simple cycles of lengths $`a`$ and $`b`$ connected at their junctions by a bridge path of length $`\ell`$. At $`\ell=0`$ the cycles share a junction. In the [single-photon model](model.md), each edge carries a unitary polarization transport and each station has an unknown local frame. Write $`A`$ and $`B`$ for the cycle holonomies at the two junctions, and let $`P`$ transport polarization from the first junction to the second. Then $`C=P^\dagger B P`$ is the second holonomy in the first junction's frame. The same local frame change conjugates $`A`$ and $`C`$.

## From twirled states to closed walks

The single-copy polarization space at each station is $`\mathbb C^d`$. Write $`\rho_{vu}`$ for the block of the single-copy density operator that maps polarization at $`u`$ to polarization at $`v`$. Its diagonal blocks are scalar, and on an edge it is a fixed scalar times a unitary. Reverse edges carry the adjoint transport. A copy is a labeled time bin with exactly one photon somewhere in the network, so $`k`$ copies have the tensor-product state space $`\mathcal H^{\otimes k}`$, where $`\mathcal H=\bigoplus_v\mathbb C^d`$.

Let $`D_g=\bigoplus_v g_v`$ collect the independent local $`U(d)`$ frame changes. The Haar-averaged $`k`$-copy state is

```math
\Omega_k(\rho)
=\int D_g^{\otimes k}\rho^{\otimes k}(D_g^\dagger)^{\otimes k}\,\prod_v dg_v .
```

**Closed-walk criterion.** Two such averaged states agree through copy number $`k`$ exactly when their closed-walk block traces agree for every walk of length at most $`k`$. A stay at a station counts as one step and uses its diagonal block.

To prove the criterion, decompose $`\mathcal H^{\otimes j}`$ for $`j\le k`$ into spatial strings $`\mathbf u=(u_1,\ldots,u_j)`$. The block of a frame-invariant observable between two such strings can be nonzero only when the strings have the same number of occurrences of each station. This follows by applying the independent central $`U(1)`$ phases of the $`g_v`$. On a pair of strings with matching counts, group the polarization factors by station. Schur–Weyl duality makes the intertwiners at each station linear combinations of permutations of the ordered polarization factors at that station. This spanning statement holds even if a station has more occurrences than $`d`$.

When paired with the corresponding block of $`\rho^{\otimes j}`$ under the trace, each such product of permutations routes the polarization index at the output of a block $`\rho_{v_i u_i}`$ to an input index from the same station. Each block has exactly one successor and one predecessor. The resulting permutation of the $`j`$ block factors splits into cycles, with an index contraction of the form

```math
\operatorname{tr}\!\left(\rho_{w_m w_{m-1}}\cdots\rho_{w_2 w_1}\rho_{w_1w_0}\right),
\qquad w_m=w_0,
```

for each cycle. The lengths add up to $`j`$. Nonedge steps give zero. Thus all invariant-observable expectations are linear combinations of products of the claimed traces. Averaging a general observable over the group turns it into an invariant observable and leaves its expectation on $`\Omega_j`$ unchanged. This proves equality of the averaged density operators. Conversely, for any chosen length-$`j`$ walk, use its start and end station strings in a single spatial block and choose the cyclic routing of polarization factors along the walk. This invariant operator has expectation equal to that walk trace. Its Hermitian and anti-Hermitian parts recover the real and imaginary components, so equality of the averaged states gives equality of that trace. The trace-generating structure also appears in the [Le Bruyn–Procesi theorem for quiver invariants](https://arxiv.org/abs/2312.08527).

## Two SU(2) rotation axes

Use the convention $`A=\cos\alpha\,I+i\sin\alpha\,\hat a\cdot\boldsymbol\sigma`$ and $`C=\cos\beta\,I+i\sin\beta\,\hat c\cdot\boldsymbol\sigma`$, with known $`\alpha,\beta\in(0,\pi)`$ and unit axes. The angles refer to a choice of orientation on each cycle. Reversing one cycle replaces its holonomy by its inverse and negates its axis under this convention. Fix the two orientations when defining $`\eta=\hat a\cdot\hat c`$.

For each closed walk, factor out the scalar weights before simplifying the unitary product. Stationary steps contribute identities. Immediate edge reversals cancel at the unitary level, including reversals across the start of the closed walk by cyclicity of the trace. In a reduced walk, entering a cycle from its junction requires a whole traversal before returning. Likewise, entering the bridge requires reaching its other junction before turning. A walk that traverses both cycles therefore uses at least $`a+b`$ cycle edges and at least $`2\ell`$ bridge edges. Shorter walks reduce either to the identity or to powers of a single holonomy, up to conjugation. Their traces depend only on the fixed angles. The scalar weights of the original walk are fixed across the alternatives.

For

```math
L=a+b+2\ell,
```

the criterion gives $`\Omega_k(\eta)=\Omega_k(\eta')`$ for all $`k\lt L`$ and all $`\eta,\eta'\in[-1,1]`$. No measurement, even a joint measurement across all stations, can distinguish those states. If frames are treated as arbitrary nuisance parameters instead of Haar draws, this equality still rules out a uniform guarantee over fresh, unconstrained frames in each window. An estimator with such a guarantee would also work after averaging each window independently. Frames stable across windows, calibrated reference signals, and extra photons in a time bin are different models.

A walk of length $`L`$ can traverse both cycles and the bridge in both directions. Choose directions so that its polarization trace is $`\operatorname{tr}(AC)`$. Pauli multiplication gives

```math
\operatorname{tr}(AC)
=2\bigl(\cos\alpha\cos\beta-\eta\sin\alpha\sin\beta\bigr).
```

With nonzero edge weights, the [local receiver](receiver.md) reads this real trace up to a known nonzero scalar. Thus its outcome distribution identifies $`\eta`$ at the threshold. This statement concerns copies available in one window. The number of repeated windows needed for a given estimation error also depends on the edge visibilities and the measurement variance.
