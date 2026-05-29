rubrica = []

while True:
    nome = input("Inserisci il nome (o 'end' per terminare): ").strip()
    if nome == "end":
        break
    if nome == "":
        print("Errore: il nome non può essere vuoto.")
        continue

    cognome = input("Inserisci il cognome: ").strip()
    if cognome == "":
        print("Errore: il cognome non può essere vuoto.")
        continue

    telefono = input("Inserisci il numero di telefono: ").strip()
    # Rimuovo eventuali spazi interni e un prefisso '+' iniziale per il controllo
    telefono_check = telefono.replace(" ", "")
    if telefono_check.startswith("+"):
        telefono_check = telefono_check[1:]
    if not telefono_check.isdigit():
        print("Errore: il numero di telefono deve contenere solo cifre (è ammesso un '+' iniziale).")
        continue
    if not (6 <= len(telefono_check) <= 15):
        print("Errore: il numero di telefono deve avere tra 6 e 15 cifre.")
        continue

    contatto = (nome, cognome, telefono)
    rubrica.append(contatto)

# Riordina solo per cognome
rubrica.sort(key=lambda c: c[1].lower())

# Stampa la rubrica
print("\n--- RUBRICA TELEFONICA ---")
if not rubrica:
    print("Nessun contatto inserito.")
else:
    for nome, cognome, telefono in rubrica:
        print(f"{cognome} {nome}: {telefono}")