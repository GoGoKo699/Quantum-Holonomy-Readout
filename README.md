# Quantum Holonomy Readout

**Can a polarized photon stream reveal whether two distant loop rotations commute when the stations have independent, unknown frames?** For two loops of lengths $`a`$ and $`b`$ joined by a bridge of $`\ell`$ edges, **$`L=a+b+2\ell`$ photons in one frame-stable window are necessary and sufficient** for the window to carry information about their relative polarization axes, with the individual loop spectra fixed and nondegenerate.

Two triangles joined by one edge need **eight photons**. A local receiver pairs time bins with balanced beam splitters, counts photons, and multiplies the signed outputs. Every optical delay is at most **two time-bin spacings**, independent of the window length. No light travels between stations during the readout.

| Result | Scope |
| --- | --- |
| Exact photon threshold $`L`$ | Independent local $`U(2)`$ frames, renewed between windows |
| Two-bin maximum delay | Station-local polarization-insensitive beam splitters and number-resolving detectors |
| Matched weak-visibility cost | Order $`\epsilon^{-2L}`$ independent windows at fixed graph, error probability, and separated hypotheses |
| Exact $`2L`$ example | Four internal modes can conceal noncommutation after the first mixed loop trace becomes accessible |

The source supplies one spatially delocalized photon per selected bin. Each frame stays fixed across the full window. The receiver delays short pairs within that window. Its exact score law makes the small accepted-event probability and the weak-visibility cost explicit.

## Read the result

| What to read | Where to start |
| --- | --- |
| Source model and definitions | [Model](science/model.md) |
| Why fewer photons cannot distinguish the axes | [Threshold proof](science/threshold.md) |
| Local optics and the two-bin schedule | [Receiver](science/receiver.md) |
| Acquisition cost, frame drift and unequal loss | [Robustness](science/robustness.md) |
| Four-mode example | [Noncommutation](science/noncommutation.md) |
| A worked example and 30 learning milestones | [Learning route](learning/README.md) |
| Quantum closure phase and polarimetric antecedents | [Related work](references/RELATED_WORK.md) |

Run the finite checks from the repository root.

```sh
python -m pip install -r verification/requirements.txt
python verification/check_holonomy.py
```

The [verification guide](verification/README.md) lists the tested instances. The [scientific account](science/README.md) gives the general proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
