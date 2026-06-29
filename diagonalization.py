import numpy as np
import sympy as sp
import scipy as sc

def d_n(mat, tol=1e-12):
   
    m = np.asarray(mat, dtype=np.complex128)
    
    if np.allclose(mat, mat.conj().T, atol=tol):
        evals,evecs = np.linalg.eigh(m)
    else:
        evals,evecs = np.linalg.eig(m)

    idx = np.argsort(evals)
    evals = evals[idx]
    evecs = evecs[:,idx]
    return evals,evecs

def d_e(mat):
    
    m = sp.Matrix(mat)
    eig_data = m.eigenvects()
    return eig_data


def f_r(evals, evecs, decimals=12):#formatting numeric eigenvalues and eigenvectors

    lines = []
    for i, val in enumerate(evals):
        vec = evecs[:, i]
        lines.append(f"Eigenvalue {i + 1}: {val:.{decimals}g}")
        lines.append(f"Eigenvector {i + 1}: {np.array2string(vec, precision=decimals, separator=', ')}")
        lines.append("")
    return "\n".join(lines)


def format_exact_result(eig_data):#formatting numeric eigenvalues and eigenvectors
    lines = []
    for i, (eigval, mult, vecs) in enumerate(eig_data, start=1):
        lines.append(f"Eigenvalue {i}: {eigval} (multiplicity {mult})")
        for j, vec in enumerate(vecs, start=1):
            lines.append(f"  Eigenvector {j}: {vec}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print("Matrix diagonalization utility")
    print("Enter a square matrix with rows separated by semicolons and values separated by spaces or commas.")
    print("Example: 1 2; 2 1")
    raw = input("Matrix: ")

    try:
        rows = [row.replace(',', ' ').strip().split() for row in raw.split(';') if row.strip()]
        matrix = np.array([[complex(x) for x in row] for row in rows], dtype=np.complex128)
    except Exception as exc:
        raise ValueError("Unable to parse matrix input.") from exc

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix.")

    print("\nNumeric diagonalization:")
    evals, evecs = d_n(matrix)
    print(format_numeric_result(evals, evecs))

    if _SYMPY_AVAILABLE:
        print("Exact symbolic diagonalization (SymPy):")
        try:
            eig_data = d_e(matrix)
            print(format_exact_result(eig_data))
        except Exception as exc:
            print("SymPy exact diagonalization failed:", exc)
    else:
        print("SymPy not installed; exact diagonalization is unavailable.")
