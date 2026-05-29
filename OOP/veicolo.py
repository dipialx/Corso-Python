class Veicolo:
    """Classe base con gli attributi comuni a ogni veicolo."""

    def __init__(self, marchio, modello, anno):
        self.marchio = marchio
        self.modello = modello
        self.anno = anno

    def stampa_info(self):
        # Es: "Toyota Corolla (2022)"
        print(f"{self.marchio} {self.modello} ({self.anno})")

    def set_marchio(self, marchio):
        self.marchio = marchio
    def set_modello(self, modello):
        self.modello = modello
    def set_anno (self, anno):
        self.anno=anno

    def get_marchio(self):
        return self.marchio
    def get_modello(self):
        return self.modello
    def get_anno(self):
        return self.anno
