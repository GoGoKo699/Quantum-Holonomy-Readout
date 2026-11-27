# Project understanding map

The first **12 background and preliminaries milestones** join the photon, graph and reference-frame models into one experimental question. The final **18 narrative and innovation milestones** follow the converse through its local contractions and the receiver through its local optical operations, then connect both to sampling and extensions.

Use the [Bartlett–Rudolph–Spekkens bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) for the reference-frame background and the [worked example](WALKTHROUGH.md) to see the full operation for two triangles.

## Phase I — Background and preliminaries

### M01 One photon across six stations

**Question.** What is the state space of a photon whose station and polarization are both uncertain?

**Understanding target.** Read the direct sum over stations and its two-dimensional polarization blocks. Distinguish a single delocalized photon from one photon at each station.

**Dependencies and connections.** Start by locating one specimen and its internal degree of freedom.

**Sources.** [State model](../science/model.md)

### M02 Density matrices and spatial coherence

**Question.** Which matrix blocks are visible to a photon counter at a single station?

**Understanding target.** Distinguish the diagonal probability blocks from off-diagonal coherences that couple stations. Explain why the uniform local marginal carries no link rotation.

**Dependencies and connections.** M01. Move from the space of one specimen to the entries of its state.

**Sources.** [State model](../science/model.md)

### M03 Polarization transport on an edge

**Question.** How does a link matrix connect two local polarization spaces?

**Understanding target.** Track the map and its adjoint when an edge is reversed. Explain why a short trip along an edge and back is the identity for the unitary link model.

**Dependencies and connections.** M01–M02. Identify the unitary inside an off-diagonal block.

**Sources.** [Link blocks](../science/model.md)

### M04 Unknown phases and occupation counts

**Question.** How can an unknown optical phase erase coherence between some configurations?

**Understanding target.** Use the center of each local unitary group to identify which terms acquire a relative phase. Derive the need for equal bra and ket occupation counts at each station.

**Dependencies and connections.** M01–M03. Use a scalar phase to isolate the first effect of local frame uncertainty.

**Sources.** [Anchor §II.B](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Converse](../science/threshold.md)

### M05 Polarization frames as a product group

**Question.** What is independently unknown at different stations?

**Understanding target.** Describe a station's optical phase and polarization convention by one unitary in U(2), and combine station actions by a block-diagonal unitary.

**Dependencies and connections.** M03–M04. Extend scalar phase uncertainty to local polarization rotations.

**Sources.** [Anchor §II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Model](../science/model.md)

### M06 One frame for every bin in a window

**Question.** What changes when the same unknown frame acts on multiple photons?

**Understanding target.** Distinguish averaging once after forming a tensor power from averaging each copy independently. Identify the correlations preserved by the common draw.

**Dependencies and connections.** M04–M05. Connect one-photon transformations to a window-level model.

**Sources.** [Anchor §II.C and §III.A.2](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Model](../science/model.md)

### M07 Twirling and observable probabilities

**Question.** Why is a uniformly averaged density operator sufficient for this converse?

**Understanding target.** Explain how integrating over the unknown frame commutes with taking a measurement probability. Connect equality of twirled states to indistinguishability under any measurement.

**Dependencies and connections.** M05–M06. Connect the nuisance distribution to an operational impossibility statement.

**Sources.** [Anchor §II.C, Eq. (2.14)](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Converse](../science/threshold.md)

### M08 Directed walks and closed products

**Question.** What becomes of the local changes of basis when successive links are composed?

**Understanding target.** Track the intermediate station factors and show why the remaining change of basis conjugates a closed product. Explain why taking the trace eliminates it.

**Dependencies and connections.** M03 and M05. Construct an invariant by composing local transport.

**Sources.** [Model](../science/model.md)

### M09 Spanning trees and a bridge

**Question.** What is left of the link data after choosing frames along a tree?

**Understanding target.** Set spanning-tree transports to the identity and identify the two remaining loop rotations. Count a bridge traversal each time the walk switches between cycles.

**Dependencies and connections.** M08. Use the graph to separate coordinate choices from loop information.

**Sources.** [Converse](../science/threshold.md)

### M10 A rotation angle and its axis

**Question.** How can two polarization rotations have the same individual spectra and a different relative orientation?

**Understanding target.** Read the angle and axis in an SU(2) matrix and separate spectral information from the dot product of two transported axes.

**Dependencies and connections.** M03 and M08–M09. Identify the invariant that distinguishes the two hypotheses.

**Sources.** [Model](../science/model.md)

### M11 An optical measurement across time bins

**Question.** What can a balanced beam splitter measure at a single station?

**Understanding target.** On the one-photon subspace, interpret the two output ports as symmetric and antisymmetric combinations of two time bins. Explain how this measurement mixes time slots while preserving total photon number.

**Dependencies and connections.** M01–M04. Identify a local operation that can access selected coherences.

**Sources.** [Receiver](../science/receiver.md)

### M12 The complete sensing task

**Question.** Which resources and information are available when the experiment starts?

**Understanding target.** State the source model, common-window frames, known graph and fixed loop spectra, target relative orientation, allowed measurements and independent renewals. Separate photons per window from the number of windows used for inference.

**Dependencies and connections.** M01–M11. Join the optical, graph and group models into the precise estimation problem.

**Sources.** [Model](../science/model.md) · [Eight-photon example](WALKTHROUGH.md)

## Phase II — Narrative and innovation

### M13 Site-balanced tensor blocks

**Question.** How does one write a candidate surviving coherence across the input slots?

**Understanding target.** Represent each tensor block by its lists of bra and ket stations, and apply the occupation constraint independently at every station.

**Dependencies and connections.** M04–M07 and M12. Translate the frame model to a concrete index selection rule.

**Sources.** [Converse](../science/threshold.md)

### M14 Polarization contractions at a station

**Question.** How does a balanced local tensor lose its frame labels?

**Understanding target.** Describe how the invariant pairings connect incoming and outgoing polarization indices. Explain why a spanning set of local permutations suffices even when it has linear dependencies.

**Dependencies and connections.** M05, M07 and M13. Use the local commutant to reduce the surviving tensor tests.

**Sources.** [Anchor §II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Converse](../science/threshold.md)

### M15 Trace products from contractions

**Question.** Why does a local pairing lead to a collection of closed walks?

**Understanding target.** Follow one polarization index through matrix blocks and contractions until it closes. Distinguish the resulting trace on one walk from a product of traces on disjoint contractions.

**Dependencies and connections.** M08 and M13–M14. Turn an invariant of the optical state into a graph calculation.

**Sources.** [Converse](../science/threshold.md)

### M16 Cutting away backtracking

**Question.** Which directed steps contribute no new loop information?

**Understanding target.** Remove immediate opposite traversals and reduce a closed word cyclically. Explain why erasing a backtrack preserves its trace and shortens its needed walk.

**Dependencies and connections.** M03, M09 and M15. Couple word reduction to the physical cost per edge step.

**Sources.** [Converse](../science/threshold.md)

### M17 Two separate traces versus one mixed trace

**Question.** Can learning the spectra of both loops determine their relative axis?

**Understanding target.** Show that single-loop powers and products of their traces depend only on individual spectra. Identify a mixed trace as the first kind of contraction that can distinguish the chosen axes.

**Dependencies and connections.** M10 and M15–M16. Locate the information missing from separate loop measurements.

**Sources.** [Converse](../science/threshold.md)

### M18 The bridge cost

**Question.** What is the shortest walk that can compare the two axes?

**Understanding target.** Derive the cost of one full winding of each cycle and two full bridge crossings. Explain why a short excursion into the bridge contributes no relative information.

**Dependencies and connections.** M09 and M16–M17. Establish the graph bound on informative contractions.

**Sources.** [Converse](../science/threshold.md)

### M19 Why too few photons give no information

**Question.** How does a shortest-walk statement constrain every possible receiver?

**Understanding target.** Use the length of every contraction to show exact equality of the window states below the threshold. Extend equality to any collection of independent, undersized windows.

**Dependencies and connections.** M07, M12 and M15–M18. Turn the graph bound into the full measurement converse.

**Sources.** [Converse](../science/threshold.md)

### M20 Matching temporal pairs to the walk

**Question.** How is a closed walk converted into local optical settings?

**Understanding target.** Assign a time bin to each directed step and pair the preceding and current step bins at each station occurrence. Account for repeated visits without using a station-time mode twice.

**Dependencies and connections.** M11, M15 and M18. Translate the first informative invariant into optical mode pairings.

**Sources.** [Receiver](../science/receiver.md) · [Worked schedule](WALKTHROUGH.md)

### M21 The two compatible photon patterns

**Question.** Which input patterns can survive every local one-photon test?

**Understanding target.** Propagate the one-photon constraint from one time-bin pair to the next. Recover the two consistent global patterns and see how the parity observable connects them.

**Dependencies and connections.** M13 and M20. Show how local counting constraints select a single closed contraction.

**Sources.** [Receiver](../science/receiver.md) · [Eight-photon example](WALKTHROUGH.md)

### M22 From port parity to relative angle

**Question.** What does the product of detector signs estimate?

**Understanding target.** Relate the parity expectation to the real mixed trace. Use the known loop angles to recover the dot product of the transported axes from the mean.

**Dependencies and connections.** M10 and M20–M21. Identify the physical data and the estimand.

**Sources.** [Receiver](../science/receiver.md)

### M23 Folding the time-bin order

**Question.** Why can a long walk have a short optical delay?

**Understanding target.** Assign increasing odd labels and decreasing even labels around the walk. Check the delay bound on both transitions between the runs and distinguish it from the frame-stability demand.

**Dependencies and connections.** M06 and M20. Separate the nuisance coherence window from the storage of one optical mode.

**Sources.** [Receiver](../science/receiver.md) · [Worked schedule](WALKTHROUGH.md)

### M24 Two triangles with one bridge

**Question.** What does the complete receiver do for aligned and orthogonal axes?

**Understanding target.** Trace the eight-step walk, work out the splitter list and compare the two parity distributions. Explain what eight photons make possible and why many such windows can still be necessary.

**Dependencies and connections.** M19 and M21–M23. Assemble the first nontrivial experiment from its input to its output.

**Sources.** [Eight-photon example](WALKTHROUGH.md)

### M25 Signal, accepted events and statistical cost

**Question.** How do the acceptance probability and the conditional sign bias determine the data cost?

**Understanding target.** Distinguish nonzero scores from informative sign imbalance. Explain the weak-visibility cost at fixed graph and why the exact copy threshold alone does not bound the number of trials.

**Dependencies and connections.** M21–M24. Relate the optical resource threshold to estimation accuracy.

**Sources.** [Robustness and statistics](../science/robustness.md)

### M26 Stability and source departures

**Question.** Which assumptions must an optical realization check?

**Understanding target.** Identify the local mode-overlap and frame-stability requirements. Trace how drift enters paired interference, and distinguish known losses from multiphoton and detector errors.

**Dependencies and connections.** M06, M11 and M23–M25. Connect ideal proofs to separately specified nonideal source and receiver models.

**Sources.** [Robustness and statistics](../science/robustness.md)

### M27 From relative axes to noncommutation

**Question.** How does a loop product report whether two transports commute?

**Understanding target.** Relate the trace of the group commutator to the Frobenius norm of the matrix commutator. Identify why the walk compares the loops more than once.

**Dependencies and connections.** M10, M17 and M20–M22. Reuse the receiver for a different invariant.

**Sources.** [Noncommutation](../science/noncommutation.md)

### M28 A dimension-four discrimination example

**Question.** Can a mixed trace of two loops agree even when their commutation properties differ?

**Understanding target.** Track the matched individual spectra and matched first mixed trace for the two involution pairs. Explain why the shorter invariants agree and a doubled walk separates them.

**Dependencies and connections.** M16–M19 and M27. Apply the same threshold reasoning to a higher-dimensional promise family.

**Sources.** [Noncommutation](../science/noncommutation.md)

### M29 Reading theory and verification together

**Question.** Which scientific evidence supports the receiver and which supports the converse?

**Understanding target.** Distinguish the mathematical spanning argument from finite enumeration and receiver checks. Relate the result to known frame twirling while assigning the graph threshold and acquisition design to this project.

**Dependencies and connections.** M14, M19 and M24–M28. Identify what each proof and numerical check can establish.

**Sources.** [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Verification script](../verification/check_holonomy.py)

### M30 The complete acquisition tradeoff

**Question.** What fixes the size of a useful window and what fixes the delay and trial count?

**Understanding target.** Synthesize the exact graph threshold, same-window frame promise, paired delay bound, and weak-visibility cost. State the conclusion for the ideal model and identify the assumptions to revisit for a new source.

**Dependencies and connections.** M01–M29. Connect graph geometry to the operational resources of polarized-light readout.

**Sources.** [Model](../science/model.md) · [Converse](../science/threshold.md) · [Receiver](../science/receiver.md) · [Robustness](../science/robustness.md)
