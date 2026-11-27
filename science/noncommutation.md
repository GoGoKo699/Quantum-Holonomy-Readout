# Testing noncommutation

The [two-axis threshold](threshold.md) applies to fixed-angle $`SU(2)`$ holonomies. The same graph and receiver support a different exact threshold when each station has four internal modes. In dimension four, the individual spectra and the shortest mixed trace can agree even when one pair commutes and the other does not.

## A receiver for the commutator trace

Let $`A`$ and $`C`$ be the two unitary holonomies in a common junction frame. Their commutator as a difference of products satisfies

```math
\|AC-CA\|_{\mathrm F}^{2}
=2d-2\operatorname{Re}\operatorname{tr}(ACA^\dagger C^\dagger).
```

This follows by expanding the squared Frobenius norm and using unitarity and cyclicity of the trace. In particular, the real commutator trace equals $`d`$ exactly when the holonomies commute. Realize its ordered product by traversing each cycle once in each direction and crossing the bridge four times. The resulting closed walk has length $`2L=2a+2b+4\ell`$. The [local receiver](receiver.md) applies to repeated visits to the same station because consecutive walk vertices are distinct and the two-bin pairs at each station are disjoint. Its mean identifies the real commutator trace after rescaling by the known nonzero edge weights. The statement is about identifiability. A statistical test can distinguish separated alternatives by repeating the receiver over independent windows.

## A sharp four-mode example

Let $`X`$ and $`Z`$ be the usual Pauli matrices and choose the transports so that the common-frame holonomies are

```math
A=Z\oplus(-Z),\qquad C_0=Z\oplus Z,\qquad C_1=X\oplus X.
```

For example, put the identity on every bridge edge and on all but one edge of each cycle. All three displayed matrices are determinant-one involutions. The alternatives have the same two cycle spectra, and $`\operatorname{tr}(AC_0)=\operatorname{tr}(AC_1)=0`$. The first pair commutes and the second anticommutes. Correspondingly,

```math
\operatorname{tr}(AC_0AC_0)=4,\qquad
\operatorname{tr}(AC_1AC_1)=-4.
```

For the converse, factor out the original walk's scalar edge weights and remove stationary steps and immediate reversals as in the [closed-walk criterion](threshold.md#from-twirled-states-to-closed-walks). In the cyclic list of complete cycle traversals, each letter is now $`A`$ or $`C_j`$, for $`j=0,1`$. Its orientation is immaterial because the chosen holonomies equal their inverses. Remove consecutive equal letters in pairs, including across the cyclic boundary. A surviving word is empty, a single letter, or an even alternating word. The empty, one-letter and two-letter traces agree between the alternatives. A surviving word of length at least four requires at least two full traversals of each original cycle. The surviving letters form a cyclically ordered subsequence of the original traversals. Each segment between successive surviving letters connects opposite junctions and hence crosses the bridge. Any such walk has length at least $`2a+2b+4\ell`$.

Thus every closed-walk trace of length less than $`2L`$ agrees in the two alternatives. The twirled states are identical below $`2L`$ copies, even for unrestricted joint measurements. The commutator trace distinguishes them at $`2L`$, proving sharpness in dimension four for the stated resetting-frame model. The example establishes a worst-case threshold. Some holonomy pairs can be distinguished using shorter walks.
