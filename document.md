# Documentation of CodeBase
This is a Python Codebase for calculation on Finite Conjugated Systems enabled by  semiemperical Hamiltonian Models. This codebase deploys second quantisation formalism for its ability to represent many body systems with ease.

## Components of The CodeBase
1. Interface
2. Basis and operations
3. Hamiltonians 
4. Huckel

### 1. Interface
this folder contains the code that powers the whole calculation interface of this CodeBase

session.py file keeps track contains a dictionary which keeps track of important variables(given by users and created by program)  
Some variables are initially prompted to be given by users, and used further in calculations which includes the no. of Spin orbitals, no. of electrons, Semi emperical Parameters,etc  
run_c.py is the go to file to run calculations 