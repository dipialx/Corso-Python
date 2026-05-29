from auto import Auto
from moto import Moto

def conta_auto_elettriche(veicoli):
    """Restituisce quante auto elettriche sono presenti nella lista."""
    return sum(
        1 for v in veicoli
        if isinstance(v, Auto) and v.alimentazione == "Elettrica"
    )


def trova_veicolo_piu_potente(veicoli):
    """Restituisce il veicolo con più cavalli (None se la lista è vuota)."""
    if not veicoli:
        return None
    return max(veicoli, key=lambda v: v.cavalli)


def media_cavalli(veicoli):
    """Restituisce la media dei cavalli di tutti i veicoli (0 se lista vuota)."""
    if not veicoli:
        return 0
    return sum(v.cavalli for v in veicoli) / len(veicoli)

veicoli = []

# Almeno 3 automobili
veicoli.append(Auto("Tesla", "Model 3", 2024, "Elettrica", None, 283, 4, True, 425))
veicoli.append(Auto("Toyota", "Corolla", 2022, "Benzina", 1600, 132, 5, True, 470))
veicoli.append(Auto("Volkswagen", "Golf", 2021, "Diesel", 2000, 150, 5, False, 380))

# Almeno 3 motociclette
veicoli.append(Moto("Yamaha", "MT-07", 2023, "Benzina", 689, 73, "Naked", False))
veicoli.append(Moto("Honda", "Africa Twin", 2022, "Benzina", 1084, 102, "Enduro", True))
veicoli.append(Moto("Piaggio", "Vespa GTS 300", 2023, "Benzina", 278, 24, "Scooter", True))

# Polimorfismo: lo stesso metodo si comporta diversamente per ogni classe
print("=" * 40)
print("ELENCO VEICOLI")
print("=" * 40)
for veicolo in veicoli:
    veicolo.stampa_info()
    print("-" * 40)

# Funzioni di analisi sulla lista
print("\n" + "=" * 40)
print("STATISTICHE")
print("=" * 40)
print(f"Auto elettriche: {conta_auto_elettriche(veicoli)}")

piu_potente = trova_veicolo_piu_potente(veicoli)
print(f"Veicolo più potente: {piu_potente.marchio} {piu_potente.modello} ({piu_potente.cavalli} CV)")

print(f"Media cavalli: {media_cavalli(veicoli):.1f} CV")