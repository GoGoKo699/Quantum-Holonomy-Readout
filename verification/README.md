# Verification

Run from the repository root with Python 3 and NumPy.

```sh
python -m pip install -r verification/requirements.txt
python verification/check_holonomy.py
```

| Check | Scope |
| --- | --- |
| Optical pairing and schedule | Enumerates 131,064 binary assignments to pairs for lengths 3 through 16. Checks the two compatible assignments and the maximum delay. |
| Polarization model | Checks the source preparation mixture, finite gauge transformations and first differing traces on six two-cycle graphs. |
| Score moments | Evaluates the compressed score operator on the two compatible station strings for six- and eight-step walks. |
| Four-mode noncommutation | Checks the commuting versus anticommuting example and the first differing trace on six two-cycle graphs. |

A successful run prints one summary per check and exits zero. These finite computations supplement the analytical [threshold](../science/threshold.md) and [receiver](../science/receiver.md) proofs.
