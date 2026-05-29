b=19

def saluta():
    global b
    a=23
    b=b+5
    # Blocco indentato di 4 spazi appartenente alla funzione
    print("Ciao!") 
print("Benvenuto in Python.")

# Blocco principale (fuori dalla funzione)

print("Programma avviato")
saluta()
saluta()
saluta()

