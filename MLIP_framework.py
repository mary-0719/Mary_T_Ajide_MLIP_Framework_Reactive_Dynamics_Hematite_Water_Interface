 

# ------------------------------------------------------------------------------
# Script Name: Overall_methodological_framework.py

# Title: Framework for Machine-Learning Interatomic Potential Simulations of the Hematite–Water Interface 

# Description: To capture molecular adsorption, water dissociation, and associated electronic-structure changes at the hematite–water interface, we developed a machine-learning interatomic potential (MLIP) framework that integrates first-principles data generation, active learning, long-timescale molecular dynamics, and quantum-mechanical validation. The framework consists of six interconnected modules described below.

# Author: [Mary Taiwo Ajide]
# Affiliation: [University College Dublin]
# Contact: [mary.ajide19@gmail.com]
#
# Created: [1st December 2025]
# Last Updated: [3rd December 2025]
#
# Copyright © [2025] [Mary T. Ajide]. All rights reserved.
#
# This script is original work by the author. Unauthorised use, duplication,
# or distribution without explicit permission is prohibited. Portions of this
# code may be adapted or reused for research purposes with proper citation
# and attribution.
#
# If used in scientific publications, please cite: [Mary T. Ajide], et al., "[Title]",
# [Journal], [Year].
# ------------------------------------------------------------------------------

┌────────────────────────────────────────────────────────┐
 │         1. First-Principles Data Generation            │
 ├────────────────────────────────────────────────────────┤
 │ • AIMD sampling with SCAN                              │
 │ • Diverse adsorption/dissociation snapshots            │
 │ • Energies / forces / stresses → reference dataset     │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │        2. MLIP Training & Optimisation                 │
 ├────────────────────────────────────────────────────────┤
 │ • VASP MLFF training                                   │
 │ • Descriptor selection                                 │
 │ • Parameter optimisation                               │
 │ • Sparsification + uncertainty estimation              │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │      3. Active Learning & Data Selection               │
 ├────────────────────────────────────────────────────────┤
 │ • MLMD exploration                                     │
 │ • Identify high-uncertainty structures                 │
 │ • Re-evaluate with DFT                                 │
 │ • Augment dataset → retrain                            │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │      4. ML-Accelerated Molecular Dynamics              │
 ├────────────────────────────────────────────────────────┤
 │ • Long MD (ps–tens of ps)                              │
 │ • Adsorption & dissociation events                     │
 │ • Hydration-layer evolution                            │
 │ • Proton transfer                                      │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │      5. Structural & Dynamical Validation              │
 ├────────────────────────────────────────────────────────┤
 │ • Radial distribution functions (RDFs)                 │
 │ • Mean-squared displacement (MSD)                      │
 │ • Coordination environments                            │
 │ • Comparison of MLMD vs DFT benchmarks                 │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │          6. Electronic-Structure Validation            │
 ├────────────────────────────────────────────────────────┤
 │ • DOS/PDOS                                             │
 │ • Charge-density difference                            │
 │ • Fe–O / O–H bonding                                   │
 │ • Mechanistic verification with DFT                    │
 └────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌────────────────────────────────────────────────────────┐
 │        7. Structural & Mechanistic Analysis            │
 ├────────────────────────────────────────────────────────┤
 │ • Classify molecular vs dissociative species           │
 │ • Proton-transfer pathways                             │
 │ • Interface layering                                   │
 │ • Mechanistic reconstruction                           │
 └────────────────────────────────────────────────────────┘
