from veicolo import *

#stampaCoseStrane()


class Moto(Veicolo):
    """Una motocicletta. Eredita da Veicolo e aggiunge i propri attributi."""

    def __init__(self, marchio, modello, anno, alimentazione, cilindrata,
                 cavalli, tipologia, ha_abs):
        super().__init__(marchio, modello, anno)
        #super.set_marchio(marchio)

        self.alimentazione = alimentazione
        self.cilindrata = cilindrata
        self.cavalli = cavalli
        self.tipologia = tipologia          # Sportiva / Touring / Naked / Scooter / Enduro
        self.ha_abs = ha_abs                # True / False


    def stampa_info(self):
        super().stampa_info()
        print(f"Tipologia: {self.tipologia}")
        print(f"Alimentazione: {self.alimentazione}")
        print(f"Cilindrata: {self.cilindrata} cc")
        print(f"Potenza: {self.cavalli} CV")
        print(f"ABS: {self.ha_abs}")

a = Moto("Yamaha", "MT-07", 2023, "Benzina", 689, 73, "Naked", True)
a.stampa_info()