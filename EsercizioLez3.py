import numpy as np

# Creazione delle due matrici
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrice A:")
print(A)
print("\nMatrice B:")
print(B)

# Somma tra A e B
print("\nSomma (A + B):")
print(A + B)

# Sottrazione A - B
print("\nSottrazione (A - B):")
print(A - B)

# Moltiplicazione elemento per elemento
print("\nMoltiplicazione elemento per elemento (A * B):")
print(A * B)

# Prodotto matriciale
print("\nProdotto matriciale (A @ B):")
print(A @ B)

# --- Operazioni opzionali ---

# Trasposta di A
print("\nTrasposta di A (A.T):")
print(A.T)

# Valore massimo e minimo di B
print("\nValore massimo di B:", B.max())
print("Valore minimo di B:", B.min())

# Somma di tutti gli elementi di A
print("\nSomma di tutti gli elementi di A:", A.sum())