from veicolo import Veicolo

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
        
        if self.cilindrata is not None: 
            # le elettriche non hanno cilindrata
            print(f"Cilindrata: {self.cilindrata} cc")

        print(f"Potenza: {self.cavalli} CV")
        print(f"Porte: {self.numero_porte}")
        print(f"Cambio automatico: {self.cambio_automatico}")
        print(f"Bagagliaio: {self.capacita_bagagliaio} L")