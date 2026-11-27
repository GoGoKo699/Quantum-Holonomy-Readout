# Source, frames and estimation task

A station receives either vacuum or one polarization register in a labeled time bin. Each bin contains one photon across the whole array. Its location can be coherent across stations. The receiver knows which time bins the source uses and can match their wave packets. It does not receive a nondestructive location label.

## The source state

Let a finite simple graph $`G`$ have $`n`$ stations and maximum degree $`\Delta`$. The one-photon space is $`\bigoplus_{v\in V(G)}\mathbb C^d`$. A matrix block with row $`u`$ and column $`v`$ maps a polarization at $`v`$ to one at $`u`$. The source is specified by

```math
\rho_{vv}=\frac{I_d}{dn},\qquad
\rho_{uv}=\frac{\epsilon}{dn}U_{uv}\quad (uv\in E(G)),\qquad
U_{vu}=U_{uv}^{\dagger}.
```

Off-diagonal blocks outside the graph vanish. The $`U_{uv}`$ are unitary and the link visibility $`\epsilon`$ is common, positive and known. The diagonal gives a uniformly random station when one measures location. The matrix $`K=(dn\,\rho-I)/\epsilon`$ has operator norm at most $`\Delta`$. Indeed, for a block vector $`x`$, the norm of $`(Kx)_u`$ is bounded by the sum of $`\lVert x_v\rVert`$ over neighbors. The scalar adjacency matrix has norm at most $`\Delta`$. Thus $`0\lt \epsilon\lt 1/\Delta`$ suffices for positivity and gives $`\rho\succeq (1-\Delta\epsilon)I/(dn)`$.

One possible preparation is a classical mixture. Choose each edge $`uv`$ with probability $`2\epsilon/n`$. For that choice, prepare

```math
\frac{|v,p\rangle+|u,U_{uv}p\rangle}{\sqrt2}
```

for a uniformly chosen basis polarization $`p`$. Alternatively choose a single station $`v`$ with probability $`(1-\epsilon\,\deg(v))/n`$ and prepare a photon there with the maximally mixed polarization. These probabilities sum to one and the mixture has the stated blocks. The estimator receives neither the mixture labels nor the preparation controls.

## Frame stability

On a window of $`k`$ bins the state is $`(D_g\rho D_g^\dagger)^{\otimes k}`$, where $`D_g=\bigoplus_v g_v`$, with $`g_v\in U(d)`$. For the converse, the frames are independently Haar drawn at the stations and independently renewed between windows. The window density matrix is then

```math
\mathcal T_k(\rho^{\otimes k})=
\int (D_g\rho D_g^\dagger)^{\otimes k}\,\prod_v dg_v.
```

Equivalently this random schedule is a prior for a worst-case guarantee over arbitrary unknown schedules. A deterministic guarantee uniform in schedules must also hold under that prior. Receiver expectations are identical for every allowed choice of fixed within-window frames. They require common time-bin labels and calibrated relative phase inside each local interferometer. They do not require a shared polarization basis, optical local oscillator or coherent coupling between stations during readout. In a different model with a stable frame linking several windows, those windows may combine to supply a longer effective window.

## Two loops and a bridge

Take two simple cycles of lengths $`a`$ and $`b`$, joined by a simple path of $`\ell`$ edges that meets the cycles only at its endpoints. For $`\ell=0`$ the cycles share one junction. Each loop has a designated orientation. Let $`A`$ and $`B`$ be their ordered link products based at the respective junctions, and let $`P`$ transport from the first junction to the second. Write $`C=P^\dagger BP`$ for the second loop in the first junction's polarization space. The closed walk that goes around the first loop, crosses the bridge, goes around the second and returns has $`L=a+b+2\ell`$ steps. Its holonomy has trace $`\operatorname{Tr}(CA)`$.

For the polarization problem $`d=2`$ and $`A,C\in SU(2)`$. Write $`A=\cos\alpha\,I+i\sin\alpha\,\hat a\cdot\sigma`$ and $`C=\cos\beta\,I+i\sin\beta\,\hat c\cdot\sigma`$, with Pauli matrices $`\sigma`$ and $`0\lt \alpha,\beta\lt \pi`$. The fixed angles specify individual loop spectra. The estimand is $`\eta=\hat a\cdot\hat c`$. In particular, $`|\eta|=1`$ gives commuting rotations and $`|\eta|\lt 1`$ gives noncommuting rotations. The comparison changes $`\eta`$ at fixed angles and visibility. The operational question is how many photons must share one frame window before any measurement can distinguish the changes.

- [Threshold proof](threshold.md)
- [Receiver and time-bin schedule](receiver.md)
- [Acquisition cost and imperfections](robustness.md)
- [Noncommutation with more internal modes](noncommutation.md)
