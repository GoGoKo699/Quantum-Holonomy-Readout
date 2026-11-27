# Measuring a closed walk with local optics

Let $`v_1,\ldots,v_L`$ be the successive stations along a closed walk, with $`v_{L+1}=v_1`$, consecutive stations distinct, and indices taken modulo $`L`$. Give the input photons logical bin labels $`1,\ldots,L`$. The receiver implements the following procedure.

1. At station $`v_i`$, route its modes in logical bins $`i-1`$ and $`i`$ to a balanced, polarization-insensitive beam splitter. Use the same port convention in every pair.
2. Count photons in the two outputs, summing over polarization. Set $`z_i=+1`$ or $`-1`$ when the corresponding output contains the pair's only photon. Set $`z_i=0`$ when the total differs from one.
3. Report $`Z=\prod_i z_i`$ after the stations exchange the counts or their signs.

Even when the same station occurs several times, its prescribed pairs are disjoint. A bin can appear in two pairs only at the two distinct stations at the ends of its walk step. A beam splitter can therefore be measured as soon as its later bin arrives.

## What the score measures

On one photon in its two input modes, the local sign observable exchanges the occupied mode and leaves the internal state untouched. Its square projects onto the one-photon sector of the pair. The score operator is the product of these local observables. Its square is the product of the one-photon projections. The product acts on disjoint optical modes.

Condition first on being in the support of the squared score. At logical bin $`i`$, the photon can be at $`v_i`$, in pair $`i`$, or at $`v_{i+1}`$, in pair $`i+1`$. Each of the $`L`$ pairs needs one photon and already consumes all $`L`$ photons. Choosing $`v_i`$ at one bin forces the same choice relative to the walk at its neighbor. Going around the logical cycle leaves exactly two station strings, $`s=(v_1,\ldots,v_L)`$ and $`t=(v_2,\ldots,v_L,v_1)`$. Since the diagonal station probabilities are $`1/n`$, the nonzero-score probability is $`2n^{-L}`$.

The simultaneous exchanges take $`s`$ to $`t`$ and back. They cyclically permute the polarized registers while moving each register between times at its own station. In the expectation against $`\rho^{\otimes L}`$, the polarization contraction on the $`s`$-to-$`t`$ block is the trace of a product of the off-diagonal blocks of the source. With the direction convention in the [model](model.md), the two terms are complex conjugates, and

```math
\begin{aligned}
H_W&= U_{v_1v_L} U_{v_L v_{L-1}}\cdots U_{v_2v_1},\\
\mu:=\mathbb E[Z]&=2\left(\frac{\epsilon}{dn}\right)^L
                  \operatorname{Re}\operatorname{Tr}(H_W),\\
q:=\mathbb E[Z^2]&=2 n^{-L}.
\end{aligned}
```

The site-frame matrices telescope in the ordered product, so $`\mu`$ is the same for every fixed frame in the window. The two sign probabilities are $`(q+\mu)/2`$ and $`(q-\mu)/2`$, and the zero probability is $`1-q`$. This calculation counts zero-score trials in the sample cost.

For two polarization loops, $`H_W=CA`$ with the conventions in the model. Thus

```math
\mathbb E[Z]=4\left(\frac{\epsilon}{2n}\right)^L
\left(\cos\alpha\cos\beta-\sin\alpha\sin\beta\,\eta\right).
```

The mean is an invertible affine function of $`\eta`$ at fixed nondegenerate eigenangles and nonzero visibility. Averaging the raw scores gives an unbiased estimator before any optional clipping of the axis dot product to its physical range. The frame window remains long enough for all $`L`$ photons to arrive.

## Two-bin delay schedule

In chronological order, label the physical arrival slots $`1,\ldots,L`$, equally spaced. Assign the successive logical indices of the walk to increasing odd slot numbers followed by decreasing even slot numbers. For $`L=8`$ the sequence of physical slot labels in logical order is

```text
1, 3, 5, 7, 8, 6, 4, 2
```

Successive entries, including the wrap from the last to the first, differ by at most two. Thus each beam splitter requires a delay of at most two bin spacings. The reassignment is valid because the copies are independent and identically prepared conditional on the window frames. It does not shorten the span over which the source supplies a common frame. The design uses $`L`$ beam-splitter measurements per trial, calibrated local interference and number resolution. Source creation and transmission to the receiver stations are separate resources.

See the [eight-photon walkthrough](../learning/WALKTHROUGH.md) for the complete station and time-bin assignment and [acquisition costs](robustness.md) for visibility, drift and loss.
