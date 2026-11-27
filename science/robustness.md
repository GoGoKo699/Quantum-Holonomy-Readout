# Weak visibility, frame drift, and photon loss

The [model](model.md) supplies one photon per input time bin on a graph with $`n`$ stations, with two polarization modes per station. Its diagonal blocks are $`I_2/(2n)`$ and its oriented link blocks are $`\epsilon U_{uv}/(2n)`$. Let $`\Delta`$ be the maximum graph degree. The quantum lower bound below concerns independent Haar frame renewals. The drift and loss results describe changes to the [local receiver](receiver.md) on the same input graph.

## Visibility cost for separated hypotheses

Fix two link assignments on the graph whose first differing Wilson trace occurs at length $`L`$. Suppose the receiver's chosen length-$`L`$ walk $`W`$ has a fixed real trace gap

```math
g=\left|\operatorname{Re}\operatorname{tr}(H_{W,0})
             -\operatorname{Re}\operatorname{tr}(H_{W,1})\right|\gt 0,
```

where $`H_{W,h}`$ is the ordered link product for hypothesis $`h`$. In the two-cycle $`SU(2)`$ model the traces are real. Keep the graph, link assignments, and copy cap $`K\ge L`$ fixed as $`\epsilon\to0`$. For $`0\lt \delta\le1/4`$, the number of independent windows required to distinguish the hypotheses with error at most $`\delta`$ under either one satisfies

```math
m^*(\epsilon,\delta)
  =\Theta\!\left(\epsilon^{-2L}\log(1/\delta)\right).
```

The constants may depend on the fixed graph, hypotheses, and $`K`$. The lower bound allows an arbitrary joint quantum measurement across the complete windows.

### Local receiver upper bound

Let $`Y\in\{-1,0,1\}`$ be the product of the signed detector outputs in a window. The two orientations of the pairing cycle give the receiver's moments

```math
\mu_h=\mathbb E_h[Y]=2\left(\frac{\epsilon}{2n}\right)^L
                      \operatorname{Re}\operatorname{tr}(H_{W,h}),
\qquad
p=\mathbb E_h[Y^2]=2n^{-L}.
```

The receiver uses $`L`$ photons in one window. Classify its empirical mean over independent windows at the midpoint of the two means. Writing $`d=|\mu_0-\mu_1|`$, Bernstein's inequality gives error at most $`\exp[-m d^2/(8(p+d/3))]`$ under each hypothesis. Since $`|\mu_h|\le p`$, the required number of windows is

```math
O\!\left(\frac{p}{d^2}\log(1/\delta)\right)
 =O\!\left(\frac{1}{g^2}\left(\frac{4n}{\epsilon^2}\right)^L
            \log(1/\delta)\right).
```

The count uses all windows, including those yielding zero, and consumes $`L`$ photons per window. The factor growing with $`n`$ and $`L`$ reflects the rarity of useful occupancy patterns. The matched exponent concerns weak visibility at fixed graph and fixed copy cap.

### Joint quantum lower bound

Write the one-copy states as $`\rho_h(\epsilon)=(I+\epsilon A_h)/(2n)`$, where $`A_h`$ is the Hermitian block adjacency matrix, with $`\|A_h\|_\infty\le\Delta`$. Let $`\sigma_h(\epsilon)`$ be the local Haar twirl of $`\rho_h(\epsilon)^{\otimes K}`$, with the same frame acting on the $`K`$ copies in a window. A full $`K`$-copy window also supplies any strategy that uses up to $`K`$ copies by discarding the extras.

Every term of degree $`s\lt L`$ in the tensor expansion of $`\sigma_0-\sigma_1`$ vanishes. For a fixed subset of $`s`$ copies, the term is the twirl of $`A_h^{\otimes s}`$ on those copies tensored with the identity on the others. This is proportional to the coefficient of $`\epsilon^s`$ in the twirled $`s`$-copy density matrix. The copy-threshold theorem gives equality of those two $`s`$-copy density matrices for all sufficiently small $`\epsilon`$. Consequently,

```math
\left\|\sigma_0-\sigma_1\right\|_\infty
 \le \frac{2}{(2n)^K}\sum_{s=L}^K {K\choose s}(\epsilon\Delta)^s,
\qquad
\lambda_{\min}(\sigma_h)
 \ge \left(\frac{1-\epsilon\Delta}{2n}\right)^K .
```

The first inequality uses contractivity of a unitary twirl in operator norm. The second follows from the one-copy lower spectral bound before twirling. Both apply, in particular, for $`0\lt \epsilon\Delta\le1/2`$.

For full-rank states $`\rho,\sigma`$, the quantum relative entropy, in natural logarithms, satisfies

```math
D(\rho\|\sigma)\le\log\operatorname{tr}(\rho^2\sigma^{-1})
\le \frac{\|\rho-\sigma\|_2^2}{\lambda_{\min}(\sigma)}.
```

For the first inequality, expand the entropy in the two eigenbases and apply Jensen's inequality to the logarithm with weights $`p_i|\langle i|j\rangle|^2`$, where $`p_i`$ is an eigenvalue of $`\rho`$. For the second, use $`\operatorname{tr}(\rho^2\sigma^{-1})=1+\operatorname{tr}[(\rho-\sigma)^2\sigma^{-1}]`$ and $`\log(1+x)\le x`$. Here $`\|\cdot\|_2`$ denotes the Hilbert–Schmidt norm. The spectral and operator-norm bounds give

```math
D(\sigma_0\|\sigma_1)
 \le \frac{4}{(1-\epsilon\Delta)^K}
       \left[\sum_{s=L}^K{K\choose s}(\epsilon\Delta)^s\right]^2
 =O(\epsilon^{2L}).
```

Independence across windows makes the joint relative entropy $`mD(\sigma_0\|\sigma_1)`$. Data processing through any binary decision with the stated errors lower bounds it by $`(1-2\delta)\log((1-\delta)/\delta)`$. This proves the sample lower bound at fixed $`K`$ and allows quantum memory and joint readout spanning all windows. For $`K\lt L`$, the two window states are equal and any number of independent windows remains uninformative.

## Deterministic bias under frame drift

Write the successive walk vertices as $`v_1,\dots,v_L`$ and let $`t_i`$ be the physical time of the input bin assigned to walk step $`i`$. Use cyclic indices, so $`v_{L+1}=v_1`$ and $`t_0=t_L`$. Receiver pair $`i`$ is at station $`v_i`$ and mixes bins $`t_{i-1}`$ and $`t_i`$. Its two modes can be delayed to overlap with at most two bin spacings of storage.

Let the frame at station $`v`$ and physical time $`t`$ be $`G_v(t)\in U(2)`$. Conditional on the frames, the bins are in a product of their one-photon states. The polarized link measured in input bin $`t_i`$ is $`G_{v_i}(t_i)U_{v_i v_{i+1}}G_{v_{i+1}}(t_i)^\dagger`$. In the optical mean, the normalized trace therefore has one mismatch factor between each two consecutive links,

```math
D_i=G_{v_i}(t_{i-1})^\dagger G_{v_i}(t_i),
\qquad
H_W^{\rm drift}=U_{v_1 v_2}D_2 U_{v_2 v_3}D_3\cdots
                 U_{v_L v_1}D_1.
```

With the same normalization $`2(\epsilon/(2n))^L`$ as above, the measured real trace has additive bias bounded by

```math
\left|\operatorname{Re}\operatorname{tr}(H_W^{\rm drift})
       -\operatorname{Re}\operatorname{tr}(H_W)\right|
 \le 2\sum_{i=1}^L\|D_i-I_2\|_\infty .
```

To obtain the bound, replace the factors $`D_i`$ by identities one at a time and use that the surrounding factors are unitary. If each station's change in operator norm per bin spacing is at most $`\eta_{\rm drift}`$, the two-bin schedule gives bias at most $`4L\eta_{\rm drift}`$. This is a bound on the normalized signal, even at weak visibility. The ideal second moment is unchanged because unitary frame transformations preserve site occupation probabilities. A known ideal gap $`g`$ remains distinguishable by the same midpoint under independent windows when the trace bias bound is below $`g/2`$. The exact copy threshold above uses frame constancy within each window and independent Haar renewals between windows.

## Photon counting and loss

Each polarization-insensitive beam splitter has two output ports. The signed result is $`+1`$ or $`-1`$ according to the occupied port if the pair contains exactly one detected photon and is zero otherwise. Counting must distinguish one photon from two even when both leave the same port. The interference also uses a calibrated local phase for each temporal pair, or a calibrated sum of those phases around the pairing cycle.

For an exact attenuation model, let $`\eta_{v,i}\in[0,1]`$ be the calibrated input transmissivity at station $`v`$ in bin $`t_i`$. Assume independent loss into vacuum, equal transmissivity for both polarizations on each mode, and ideal photon counting after the beam splitters. A loss event leaves fewer than $`L`$ photons in the entire window, forcing at least one zero pair outcome. In the no-loss contribution, the one-photon block $`\rho_{uv}`$ in input bin $`i`$ is multiplied by $`\sqrt{\eta_{u,i}\eta_{v,i}}`$. Thus the moments become

```math
\begin{aligned}
\mathbb E_h[Y]
 &=2\left(\frac{\epsilon}{2n}\right)^L
      \operatorname{Re}\operatorname{tr}(H_{W,h})
       \prod_{i=1}^L\sqrt{\eta_{v_i,i}\eta_{v_{i+1},i}},
\\
\mathbb E_h[Y^2]
 &=n^{-L}\left(\prod_{i=1}^L\eta_{v_i,i}
                    +\prod_{i=1}^L\eta_{v_{i+1},i}\right).
\end{aligned}
```

If attenuation depends only on the bin, both moments are multiplied by $`q=\prod_i\eta_i`$. For known $`q\gt 0`$, the midpoint test then needs order $`q^{-1}`$ more windows for the same weak-visibility bound. For $`q=0`$, the product statistic vanishes in this loss model. The formulas use one photon per input bin. Extra source photons, dark counts, and unresolved two-photon outputs can change the accepted-event statistics and require a separate detector model.
