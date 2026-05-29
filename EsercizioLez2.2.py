"""
Esercizio Lezione 2 — Sistema di gestione veicoli
Classi, ereditarietà, override dei metodi e polimorfismo.
"""


# ---------------------------------------------------------------------------
# Step 1 — Classe padre
# ---------------------------------------------------------------------------
class Veicolo:
    """Classe base con gli attributi comuni a ogni veicolo."""

    def __init__(self, marchio, modello, anno):
        self.marchio = marchio
        self.modello = modello
        self.anno = anno

    def stampa_info(self):
        # Es: "Toyota Corolla (2022)"
        print(f"{self.marchio} {self.modello} ({self.anno})")


# ---------------------------------------------------------------------------
# Step 2 + Step 3 — Sottoclasse Auto
# ---------------------------------------------------------------------------
class Auto(Veicolo):
    """Un'automobile. Eredita da Veicolo e aggiunge i propri attributi."""

    def __init__(self, marchio, modello, anno, alimentazione, cilindrata,
                 cavalli, numero_porte, cambio_automatico, capacita_bagagliaio):
        # Inizializza la parte comune tramite la classe padre
        super().__init__(marchio, modello, anno)
        self.alimentazione = alimentazione          # Elettrica / Benzina / Diesel / Gas
        self.cilindrata = cilindrata                # es. 1600, oppure None se elettrica
        self.cavalli = cavalli
        self.numero_porte = numero_porte
        self.cambio_automatico = cambio_automatico  # True / False
        self.capacita_bagagliaio = capacita_bagagliaio  # in litri

    def stampa_info(self):
        # Riusa la riga "Marchio Modello (Anno)" del padre...
        super().stampa_info()
        # ...e poi aggiunge i dettagli dell'auto
        print(f"Alimentazione: {self.alimentazione}")
        if self.cilindrata is not None:             # le elettriche non hanno cilindrata
            print(f"Cilindrata: {self.cilindrata} cc")
        print(f"Potenza: {self.cavalli} CV")
        print(f"Porte: {self.numero_porte}")
        print(f"Cambio automatico: {self.cambio_automatico}")
        print(f"Bagagliaio: {self.capacita_bagagliaio} L")


# ---------------------------------------------------------------------------
# Step 4 — Sottoclasse Moto
# ---------------------------------------------------------------------------
class Moto(Veicolo):
    """Una motocicletta. Eredita da Veicolo e aggiunge i propri attributi."""

    def __init__(self, marchio, modello, anno, alimentazione, cilindrata,
                 cavalli, tipologia, ha_abs, vano_casco):
        super().__init__(marchio, modello, anno)
        self.alimentazione = alimentazione
        self.cilindrata = cilindrata
        self.cavalli = cavalli
        self.tipologia = tipologia          # Sportiva / Touring / Naked / Scooter / Enduro
        self.ha_abs = ha_abs                # True / False
        self.vano_casco = vano_casco        # True / False

    def stampa_info(self):
        super().stampa_info()
        print(f"Tipologia: {self.tipologia}")
        print(f"Alimentazione: {self.alimentazione}")
        print(f"Cilindrata: {self.cilindrata} cc")
        print(f"Potenza: {self.cavalli} CV")
        print(f"ABS: {self.ha_abs}")
        print(f"Vano casco: {self.vano_casco}")


# ---------------------------------------------------------------------------
# Step 7 — Funzioni di utilità sulla lista di veicoli
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Step 5 + Step 6 — Creazione oggetti e uso polimorfico
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    veicoli = []

    # Almeno 3 automobili
    veicoli.append(Auto("Tesla", "Model 3", 2024, "Elettrica", None,
                        283, 4, True, 425))
    veicoli.append(Auto("Toyota", "Corolla", 2022, "Benzina", 1600,
                        132, 5, True, 470))
    veicoli.append(Auto("Volkswagen", "Golf", 2021, "Diesel", 2000,
                        150, 5, False, 380))

    # Almeno 3 motociclette
    veicoli.append(Moto("Yamaha", "MT-07", 2023, "Benzina", 689,
                        73, "Naked", True, False))
    veicoli.append(Moto("Honda", "Africa Twin", 2022, "Benzina", 1084,
                        102, "Enduro", True, True))
    veicoli.append(Moto("Piaggio", "Vespa GTS 300", 2023, "Benzina", 278,
                        24, "Scooter", True, True))

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
    print(f"Veicolo più potente: {piu_potente.marchio} {piu_potente.modello} "
          f"({piu_potente.cavalli} CV)")

    print(f"Media cavalli: {media_cavalli(veicoli):.1f} CV")