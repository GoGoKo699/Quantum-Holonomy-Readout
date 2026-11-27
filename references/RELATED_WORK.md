# Related work

## Quantum acquisition of closure phase

[Liu et al., Quantum-optimized phase closure for robust interferometric imaging](https://arxiv.org/abs/2610.06786) analyze scalar telescope-dependent phase corruption. Their Sec. III derives a three-photon threshold for triangular closure and gives a receiver combining number-sector postselection with Fourier interference. Appendix E treats longer scalar cycles. The shared ingredients here are site occupation sectors, same-window averaging and cyclic readout. The parameter in this repository is the relative orientation of two matrix-valued loop rotations with fixed individual spectra. Their comparison needs a walk across both loops and both directions of the bridge. The threshold-achieving receiver pairs time bins locally and uses one station-independent sign convention.

[Malvimat, Wucknitz and Saha, Intensity interferometry with more than two detectors](https://doi.org/10.1093/mnras/stt1934) show how multidetector intensity correlations can access scalar closure-phase information. Such correlations use distinct optical statistics from the supplied independent one-photon temporal modes in this repository. The model in this repository charges every input bin and accounts for the rare score support. It leaves a thermal-light comparison with multiphoton sectors open.

## Polarimetric closure invariants

[Broderick and Pesce, Closure Traces](https://doi.org/10.3847/1538-4357/abbd9d) introduced closure traces built from measured polarized visibilities. [Samuel, Nityananda and Thyagarajan](https://doi.org/10.1103/PhysRevLett.128.091101) formulate non-Abelian polarimetric closure invariants under general linear site distortions. [Kumar, Nityananda and Samuel](https://arxiv.org/abs/2407.00583) give a graph method for incomplete sets of measured baselines. The algebra of matrix transports and sparse graphs is therefore an antecedent. Here the receiver starts with photon states under unitary frame changes. The acquisition result asks when a particular invariant shows up in the same-window quantum density matrix and how it can be measured locally.

## Invariance and optical components

[Le Bruyn and Procesi](https://doi.org/10.1090/S0002-9947-1990-0958897-0) prove that traces of oriented cycles generate quiver invariants. The [threshold proof](../science/threshold.md) uses the corresponding tensor-level Schur–Weyl contraction argument to track the number of copies. The [reference-frame review](https://doi.org/10.1103/RevModPhys.79.555) by Bartlett, Rudolph and Spekkens supplies the physical interpretation of averaging unknown frames and is the project's [educational anchor](../learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md).

[Carosini et al.](https://arxiv.org/abs/2305.11157) demonstrate programmable interference of photons in time bins. The component needed here is a polarization-preserving balanced temporal beam splitter with calibrated relative phase and photon number resolution. The [delay schedule](../science/receiver.md#two-bin-delay-schedule) follows from how the copies are assigned to the closed walk.

## Related state-copy task

[Quantum Holonomy Sampling](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling) estimates a scalar Bargmann phase using labeled pure-state copies and coherent ray transports. The input here is a delocalized mixed state with matrix coherence between stations. Independently renewed station frames impose a per-window threshold, and the target is a relation between two transported loop rotations.
