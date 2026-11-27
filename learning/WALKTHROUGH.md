# Eight photons on two triangles

Suppose six stations share a network. Stations $`A,B,C`$ make one triangle and $`D,E,F`$ make the other. One edge joins $`A`$ to $`D`$. A window contains one photon per time bin, with two polarization modes at every station and coherence across the network. Each station uses its own unknown phase and polarization frame, held fixed within the window. The frames are independently renewed across windows.

The polarization rotation around each triangle has a known spectrum. The question is whether their axes are parallel or perpendicular after transporting them to the same station. The axes are properties of matrices accumulated around the triangles. Comparing arrows expressed in the two unaligned station frames would give a coordinate-dependent answer.

## Why the measurement needs eight photons

Each directed link matrix transports a polarization vector to its neighbor. A walk there and back applies a unitary and its inverse. A closed walk that winds only one triangle therefore gives a trace controlled by that triangle's spectrum. Reading the two traces separately cannot reveal how the transported rotations compose.

The shortest walk that winds both triangles is

```math
A\to B\to C\to A\to D\to E\to F\to D\to A .
```

It uses three edges per triangle and crosses the bridge twice. Matching local photon count and polarization indices can turn $`k`$ copies of the state into closed contractions with at most $`k`$ traversals in total. With seven or fewer photons, all those contractions are unchanged between the two hypotheses. The [converse](../science/threshold.md) explains why they determine the entire frame-averaged state and so apply to any receiver.

## What the six stations do

Number the eight edges in the displayed order. Logical slot $`j`$ supplies the photon for edge $`j`$. The station where two successive edges meet interferes the two corresponding temporal modes locally. Assign physical bin labels $`1,3,5,7,8,6,4,2`$ to the eight logical slots. The input photons have identical states within a fixed frame draw, so this assignment is a scheduling choice.

| Meeting station | Logical slots | Physical bins | Delay in bin spacings |
|---|---|---|---:|
| $`A`$, closing the walk | 8 and 1 | 2 and 1 | 1 |
| $`B`$ | 1 and 2 | 1 and 3 | 2 |
| $`C`$ | 2 and 3 | 3 and 5 | 2 |
| $`A`$, before the bridge | 3 and 4 | 5 and 7 | 2 |
| $`D`$, after the bridge | 4 and 5 | 7 and 8 | 1 |
| $`E`$ | 5 and 6 | 8 and 6 | 2 |
| $`F`$ | 6 and 7 | 6 and 4 | 2 |
| $`D`$, before the return | 7 and 8 | 4 and 2 | 2 |

Each pair uses a balanced polarization-insensitive beam splitter. Exactly one detected photon yields $`+1`$ or $`-1`$ according to the output port. Any other count yields zero. Multiply the eight local records to get the score for the window. A station visited twice uses two disjoint local mode pairs. The apparatus needs local optical mode matching and a calibrated local interference phase. Each beam splitter waits at most two bin spacings, while the station frames are common to all eight bins.

## Where the sign bias comes from

Every logical bin can contribute to exactly two of the selected pairs, at the ends of its walk edge. For all eight pairs to pass the one-photon test, every pair needs one photon. Every bin has one photon globally. A choice in one bin forces the choices in both neighboring bins, until the cycle closes. The two compatible patterns place every photon at its edge's departure station or every photon at its arrival station. The product of output signs probes the coherence connecting these two patterns. Summing the unobserved polarization index gives the trace of the eight-link product.

For a specific comparison, take the loop rotations, expressed in the same frame, to be $`R_A=i\sigma_z`$ and either $`R_D=i\sigma_z`$ or $`R_D=i\sigma_x`$. The matrices $`\sigma_x`$ and $`\sigma_z`$ are Pauli matrices for perpendicular axes. Each rotation has eigenvalues $`+i`$ and $`-i`$.

| Axis relation | Mixed trace | Mean window score at visibility $`\epsilon`$ |
|---|---:|---|
| Aligned | $`-2`$ | $`-4(\epsilon/12)^8`$ |
| Orthogonal | $`0`$ | $`0`$ |

Here $`\epsilon`$ weights the off-diagonal link blocks in the [state model](../science/model.md), and the normalization is $`2n=12`$ for six stations and two polarizations. The signed score is nonzero with probability $`2/6^8`$ in this ideal example, since the input assigns uniform station probabilities to each photon and exactly two assignments pass. The small difference in sign probabilities is the information-bearing quantity. Repeating independent windows estimates it, with many repetitions needed at weak visibility. The [receiver proof](../science/receiver.md) and [statistical analysis](../science/robustness.md) derive these moments and their implications.
