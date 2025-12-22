flowchart TD

    A[First-Principles Data Generation<br><br>
      • AIMD sampling with SCAN<br>
      • Adsorption/dissociation snapshots<br>
      • Energies/forces/stresses → dataset] --> 
    B[MLIP Training & Optimisation<br><br>
      • VASP MLFF training<br>
      • Descriptor selection<br>
      • Parameter optimisation<br>
      • Sparsification + uncertainty estimation]

    B --> C[Active Learning & Data Selection<br><br>
      • MLMD exploration<br>
      • Detect high-uncertainty structures<br>
      • Re-evaluate with DFT<br>
      • Augment dataset → retrain]

    C --> D[ML-Accelerated Molecular Dynamics<br><br>
      • Long MD (ps–tens of ps)<br>
      • Adsorption & dissociation events<br>
      • Hydration-layer evolution<br>
      • Proton transfer]

    D --> E[Electronic-Structure Validation<br><br>
      • DOS/PDOS<br>
      • Charge-density difference<br>
      • Fe–O / O–H bonding<br>
      • Validate mechanism with DFT]

    E --> F[Structural & Mechanistic Analysis<br><br>
      • Classify molecular vs dissociative species<br>
      • Proton-transfer pathways<br>
      • Interface layering<br>
      • Mechanistic reconstruction]
