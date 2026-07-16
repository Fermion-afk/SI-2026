# Codebase Documentation

## 1. Overview

This repository is a small computational toolkit for building and studying simple many-body quantum models. It is mainly used to define a physical system, choose a model Hamiltonian, build a basis of many-electron states, diagonalize the Hamiltonian, and then compute observables such as energies, eigenstates, dipole-related quantities, and response properties.

The code supports several model Hamiltonians:
- Huckel
- Hubbard
- Extended Hubbard
- PPP

The main observables that can be computed include:
- Energy eigenvalues
- Eigenstates
- Double occupancy
- Dipole moment (x and y components)
- Electron density
- Density-density correlation
- Finite-field response quantities such as polarizability, first hyperpolarizability, and second hyperpolarizability

---

## 2. Directory Structure and File Functionality

### Interface folder
The Interface folder contains the user-facing command-line workflow and the shared session state used throughout the project.

#### session.py
This is the central state manager for the whole program. It stores the current configuration for:
- the selected model
- the system setup
- the model parameters
- the basis
- the Hamiltonian matrix
- the eigenpairs

It also keeps track of whether each part is configured, created, ready, or outdated. This makes it easy for the rest of the code to know what has already been built and what needs to be recomputed.

#### model_system.py
This file handles the system configuration menu. It collects information such as:
- number of spin orbitals
- number of electrons
- boundary condition (open chain, closed ring, or neither)
- whether the system is uniform
- site coordinates and distance matrix

This is the place where the user defines the physical system before building any Hamiltonian.

#### par_hamiltonian.py
This file manages the parameter input and the core Hamiltonian workflow. It lets the user:
- set onsite energy, hopping parameter, onsite repulsion, and intersite repulsion
- construct the basis
- construct the Hamiltonian matrix
- diagonalize the Hamiltonian
- print the resulting eigenpairs

It is the main “engine” for the computation flow.

#### run_c.py
This is the main entry point of the program. It runs the top-level menu and routes the user to the model selection, system setup, parameter setup, Hamiltonian construction, observables, and finite-field response options.

#### ob_fr.py
This file contains the observable and finite-field-response routines. It provides access to:
- double occupancy
- dipole moment
- electron density
- density-density correlation
- sum-over-states response calculations
- finite-difference response calculations

---

### Basis_operations folder
This folder contains the tools for creating and manipulating the many-electron basis used in the Hamiltonian construction.

#### basis.py
This file generates basis states for a given number of spin orbitals and electrons. It can produce different excitation spaces such as:
- ground state reference
- CIS
- CISD
- CISDT
- full CI

The generated basis is then converted into a binary-hash representation for efficient manipulation.

#### binary.py
This file implements low-level bit-manipulation functions for the basis states. These are used for operations such as:
- creation and annihilation operator effects
- occupation counting
- particle-number-related checks

It is the core backend for many of the Hamiltonian-building routines.

#### operators.py
This file builds higher-level observable routines on top of the basis and binary helpers. It computes quantities like:
- expectation values
- dipole moment components
- double occupancy
- electron density
- density-density correlations

---

### Hamiltonians folder
This folder contains the model-specific Hamiltonian builders.

#### huckel.py
Builds the Huckel Hamiltonian using the chosen onsite and hopping parameters.

#### hubbard.py
Builds the Hubbard Hamiltonian, including the hopping term and onsite repulsion term.

#### ext_hubbard.py
Builds the extended Hubbard model by adding nearest-neighbor Coulomb-like interactions on top of the Hubbard model.

#### ppp.py
Builds the PPP (Pariser-Parr-Pople) Hamiltonian, which includes longer-range Coulomb interactions using the geometry of the system.

---

### Other important files
#### SOS.py
This file implements the sum-over-states approach for computing response properties such as polarizability, first hyperpolarizability, and second hyperpolarizability.

#### README.md
This file contains older project notes and usage-related information. It is useful as a supplementary reference, but the current CLI workflow is mainly driven by the Interface modules.

---

## 3. Workflow

The code flows in a fairly structured way, depending on the choices made by the user.

### Step 1: Choose the model
The user starts from the main menu and selects one of the available models:
- Huckel
- Hubbard
- Extended Hubbard
- PPP

This choice determines which Hamiltonian builder will later be used.

### Step 2: Configure the system
The user then defines the physical system:
- number of spin orbitals
- number of electrons
- boundary condition
- whether the system is uniform
- coordinates of the sites

If the model uses distance-dependent interactions, the coordinates are especially important because the program builds a distance matrix from them.

### Step 3: Set the parameters
Once the system is defined, the user enters the model parameters:
- onsite energy
- hopping parameter
- onsite repulsion
- intersite repulsion

The required parameters depend on the selected model:
- Huckel needs onsite and hopping parameters
- Hubbard needs onsite energy, hopping, and onsite repulsion
- Extended Hubbard and PPP also need intersite repulsion and geometry information

### Step 4: Construct the basis
The code uses the chosen system size and electron number to build a basis of many-electron states. This basis is stored in the shared session and later used by the Hamiltonian builder.

### Step 5: Construct the Hamiltonian
The selected Hamiltonian module is called based on the user’s previous choices. The program then builds the full Hamiltonian matrix in the chosen basis.

### Step 6: Diagonalize the Hamiltonian
The user can diagonalize the Hamiltonian in one of two ways:
- full diagonalization
- lowest-k diagonalization

This produces the eigenvalues and eigenvectors, which are then stored in the session state.

### Step 7: Compute observables or response properties
After diagonalization, the user can compute:
- observables such as double occupancy, dipole moment, electron density, and density-density correlation
- finite-field response properties such as polarizability, first hyperpolarizability, and second hyperpolarizability

### Model-dependent behavior
- Huckel is the simplest model and does not need the same interaction terms as the others.
- Hubbard includes onsite repulsion and hopping.
- Extended Hubbard adds a distance-dependent intersite interaction.
- PPP uses a more detailed long-range Coulomb treatment and depends strongly on the coordinates.

---

## 4. Template for a Sample Calculation

You can use the following template when sharing a sample run with others.

### Sample Calculation Template

**Model:**
- Example: Hubbard

**System:**
- Number of spin orbitals:
- Number of electrons:
- Boundary condition:
- Uniform system:
- Coordinates:

**Parameters:**
- Onsite energy $a$:
- Hopping parameter $b$:
- Onsite repulsion $u$:
- Intersite repulsion $v$:

**Basis:**
- Basis size:
- Basis type:

**Hamiltonian:**
- Hamiltonian matrix size:
- Main diagonal terms:
- Off-diagonal hopping terms:

**Diagonalization:**
- Method used:
- Lowest eigenvalues:
- Lowest eigenstates:

**Observables:**
- Double occupancy:
- Dipole moment (x, y):
- Electron density:
- Density-density correlation:

**Response properties (if computed):**
- Polarizability:
- First hyperpolarizability:
- Second hyperpolarizability:

### Example filled-in template

**Model:** Hubbard

**System:**
- Number of spin orbitals: 4
- Number of electrons: 2
- Boundary condition: Open Chain
- Uniform system: Yes
- Coordinates: Not required for this simple example

**Parameters:**
- Onsite energy $a$: 0.0 eV
- Hopping parameter $b$: -2.4 eV
- Onsite repulsion $u$: 8.0 eV
- Intersite repulsion $v$: Not used

**Basis:**
- Basis size: 6
- Basis type: Full CI

**Hamiltonian:**
- Hamiltonian matrix size: 6x6
- Main diagonal terms: onsite energy and Hubbard interaction terms
- Off-diagonal terms: hopping contributions

**Diagonalization:**
- Method used: full diagonalization
- Lowest eigenvalues: list them here
- Lowest eigenstates: list them here

**Observables:**
- Double occupancy: record value
- Dipole moment (x, y): record value
- Electron density: record result
- Density-density correlation: record result

---

## Summary

In short, this codebase lets you move from a physical system definition to a model Hamiltonian, then to a diagonalized quantum many-body problem, and finally to useful observables and response properties. The structure is organized around a shared session state, modular Hamiltonian builders, and a clear CLI workflow.
