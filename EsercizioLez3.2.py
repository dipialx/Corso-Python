import pandas as pd

# ============================================================
# PARTE 1 – Esplorazione del dataset
# ============================================================

# Carica il dataset in un DataFrame
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Visualizza le prime 5 righe
print("=== Prime 5 righe ===")
print(df.head())

# Visualizza le ultime 5 righe
print("\n=== Ultime 5 righe ===")
print(df.tail())

# Numero di righe e colonne
print("\n=== Numero di righe e colonne ===")
print(f"Righe: {df.shape[0]}, Colonne: {df.shape[1]}")

# Nomi delle colonne
print("\n=== Nomi delle colonne ===")
print(df.columns.tolist())

# Informazioni generali sul dataset
print("\n=== Informazioni generali ===")
df.info()


# ============================================================
# PARTE 2 – Analisi dei dati
# ============================================================

# Quanti passeggeri ci sono nel dataset?
totale = len(df)
print(f"\nPasseggeri totali: {totale}")

# Quanti passeggeri sono sopravvissuti? (Survived == 1)
sopravvissuti = (df["Survived"] == 1).sum()
print(f"Sopravvissuti: {sopravvissuti}")

# Quanti non sono sopravvissuti? (Survived == 0)
non_sopravvissuti = (df["Survived"] == 0).sum()
print(f"Non sopravvissuti: {non_sopravvissuti}")

# Età media dei passeggeri
eta_media = df["Age"].mean()
print(f"Età media: {eta_media:.2f}")

# Età massima e minima
print(f"Età massima: {df['Age'].max()}")
print(f"Età minima: {df['Age'].min()}")


# ============================================================
# PARTE 3 – Filtri
# ============================================================

# Tutti i passeggeri di sesso femminile
donne = df[df["Sex"] == "female"]
print(f"\nPasseggeri femminili: {len(donne)}")
print(donne.head())

# Tutti i passeggeri di età inferiore a 18 anni
minorenni = df[df["Age"] < 18]
print(f"\nMinorenni (< 18 anni): {len(minorenni)}")
print(minorenni.head())

# Tutti i passeggeri che sono sopravvissuti
vivi = df[df["Survived"] == 1]
print(f"\nSopravvissuti: {len(vivi)}")
print(vivi.head())

# Tutte le donne sopravvissute (doppia condizione)
donne_vive = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(f"\nDonne sopravvissute: {len(donne_vive)}")
print(donne_vive.head())


# ============================================================
# PARTE 4 – Raggruppamenti
# ============================================================

# Quanti passeggeri per sesso
print("\n=== Passeggeri per sesso ===")
print(df["Sex"].value_counts())

# Età media per sesso
print("\n=== Età media per sesso ===")
print(df.groupby("Sex")["Age"].mean())

# Quanti passeggeri per classe (Pclass)
print("\n=== Passeggeri per classe ===")
print(df["Pclass"].value_counts().sort_index())

# Tasso di sopravvivenza per classe
# La media di Survived (0/1) corrisponde alla percentuale di sopravvissuti
print("\n=== Tasso di sopravvivenza per classe ===")
print(df.groupby("Pclass")["Survived"].mean())


# ============================================================
# PARTE 5
# ============================================================

# Passeggero che ha pagato il biglietto più costoso
piu_costoso = df.loc[df["Fare"].idxmax()]
print("\n=== Biglietto più costoso ===")
print(piu_costoso[["Name", "Fare", "Pclass"]])

# I 10 passeggeri più giovani
print("\n=== 10 passeggeri più giovani ===")
piu_giovani = df.nsmallest(10, "Age")
print(piu_giovani[["Name", "Age", "Sex", "Pclass"]])

# Nuova colonna IsAdult: True se età >= 18, False altrimenti
df["IsAdult"] = df["Age"] >= 18
print("\n=== Colonna IsAdult ===")
print(df[["Name", "Age", "IsAdult"]].head())

# Salva il risultato in un nuovo file CSV
df.to_csv("titanic_modified.csv", index=False)
print("\nFile 'titanic_modified.csv' salvato correttamente.")