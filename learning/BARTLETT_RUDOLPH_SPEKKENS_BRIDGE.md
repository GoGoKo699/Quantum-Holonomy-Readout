# Reference frames and the holonomy readout

Stephen D. Bartlett, Terry Rudolph and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, **Reviews of Modern Physics 79**, 555–609 (2007). [Publisher article](https://doi.org/10.1103/RevModPhys.79.555) · [Full publisher PDF](https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.79.555/fulltext) · [Author preprint](https://arxiv.org/abs/quant-ph/0610030).

The locators below refer to the published PDF. Use it to learn how uncertainty in a reference frame transforms the state seen by a receiver. The project uses the same group averaging but asks a new question about the length of a graph walk required to compare two loop rotations.

| Read | Concept | Project connection |
|---|---|---|
| §II.B, pp. 558–560, especially Eqs. (2.5), (2.9) and (2.10) | Optical phase multiplies a number eigenstate by a number-dependent complex phase. Averaging removes coherences between distinct photon-number sectors. | Apply the phase argument to each station separately. A matrix element can survive only if its left and right station occupation counts agree. |
| §II.C, pp. 560–563, especially Eq. (2.14) and the irreducible and multiplicity decomposition that follows | Averaging conjugations by a group representation produces a twirl. Relational information may survive even when the frame is unknown. | The representation is block diagonal across stations and acts collectively across the input slots in one window. Apply the commutant result separately at each station to track what survives. |
| §III.A.2, pp. 565–567 | Several systems acted on by the same unknown rotation can carry readable information in their relations. | Compare collective polarization rotations on several carriers with independently rotating every carrier. Here the same station rotation acts on every time bin during one window. |
| §III.C.1, pp. 569–570 | Optical parties can have independent local phase conventions. | This example helps separate independent station phases from an optical operation performed entirely inside one station. |

## From one unknown frame to many

The review represents an unknown frame by a group element $`g`$ and a corresponding unitary $`T(g)`$. In this project, $`g=(g_v)_v`$ assigns a two-dimensional unitary to every station $`v`$. On the one-photon Hilbert space, the group representation is $`D(g)=\bigoplus_v g_v`$. One independent Haar draw per station defines the receiver state for a window of $`k`$ bins.

```math
\mathcal T_k(\rho^{\otimes k})
=
\int D(g)^{\otimes k}\rho^{\otimes k}
       \bigl(D(g)^\dagger\bigr)^{\otimes k}\,\mathrm dg .
```

The tensor product goes inside the integral because one draw applies throughout the window. If the stations independently redrew their frames in every bin, the integrals would instead factor across bins. The allowed input model uses the former. It starts a new independent draw when a new window begins.

## From surviving correlations to a graph invariant

A scalar station phase multiplies every ket photon at that station by the same factor and every bra photon by its conjugate. Station phases therefore erase any matrix element with unequal ket and bra counts at some station. Equal counts leave open the effect of the station's polarization rotation. At a station with matched counts, the invariant polarization contractions are spanned by pairings of ket and bra indices.

Follow one of these pairings through consecutive link matrices and back to its starting index. Summing that index gives a trace of a closed link product. Repeating the procedure gives products of traces, with total edge length bounded by the number of photons. The graph and the fixed spectra then identify the shortest contraction that can depend on the relative axes. The [converse](../science/threshold.md) gives the spanning and counting argument. The review supplies the framework for twirling and invariance. The pairing calculation and graph threshold are developed here.

## From an invariant to a measurement

A loop trace can be estimated by pairing time bins at each visited station, interfering the matching modes, and multiplying the signed detector records. The [receiver derivation](../science/receiver.md) explains why the intended contraction survives all the local photon-number tests. The [eight-photon example](WALKTHROUGH.md) turns the argument into a concrete schedule.
