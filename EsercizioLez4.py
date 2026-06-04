# -*- coding: utf-8 -*-
"""
Rubrica telefonica con wxPython.

La ListCtrl è solo la VISTA: i dati veri stanno in un dizionario di appoggio
(il MODELLO).  Ogni riga è collegata alla sua chiave nel dizionario tramite
SetItemData/GetItemData, così l'eliminazione non dipende dalla posizione.

- Form con validazione (Nome, Cognome, Telefono)
- "Aggiungi" -> inserisce nel modello e nella ListCtrl
- "Elimina"  -> rimuove la riga selezionata dal modello E dalla ListCtrl
"""

import re
import wx


class RubricaFrame(wx.Frame):

    _RE_TESTO = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ' \-]+$")

    def __init__(self):
        super().__init__(None, title="Rubrica Telefonica", size=(640, 460))

        # --- MODELLO: dizionario di appoggio --------------------------------
        # chiave = id univoco (int)  ->  valore = dict del contatto
        self._contatti = {}
        self._next_id = 0   # generatore di id univoci e stabili

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # --- Form di inserimento --------------------------------------------
        box = wx.StaticBox(panel, label="Nuovo contatto")
        form_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        grid = wx.FlexGridSizer(rows=3, cols=2, vgap=8, hgap=8)
        grid.AddGrowableCol(1, 1)

        self.txt_nome = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.txt_cognome = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.txt_telefono = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        for ctrl in (self.txt_nome, self.txt_cognome, self.txt_telefono):
            ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_aggiungi)

        grid.Add(wx.StaticText(panel, label="Nome:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.txt_nome, 1, wx.EXPAND)
        grid.Add(wx.StaticText(panel, label="Cognome:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.txt_cognome, 1, wx.EXPAND)
        grid.Add(wx.StaticText(panel, label="Telefono:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.txt_telefono, 1, wx.EXPAND)

        form_sizer.Add(grid, 0, wx.EXPAND | wx.ALL, 8)

        self.btn_aggiungi = wx.Button(panel, label="Aggiungi")
        self.btn_aggiungi.Bind(wx.EVT_BUTTON, self.on_aggiungi)
        form_sizer.Add(self.btn_aggiungi, 0, wx.ALIGN_RIGHT | wx.ALL, 8)

        main_sizer.Add(form_sizer, 0, wx.EXPAND | wx.ALL, 10)

        # --- Lista + bottone Elimina ----------------------------------------
        lista_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lista = wx.ListCtrl(
            panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN)
        self.lista.InsertColumn(0, "Nome", width=160)
        self.lista.InsertColumn(1, "Cognome", width=160)
        self.lista.InsertColumn(2, "Telefono", width=180)
        lista_sizer.Add(self.lista, 1, wx.EXPAND | wx.RIGHT, 8)

        self.btn_elimina = wx.Button(panel, label="Elimina")
        self.btn_elimina.Bind(wx.EVT_BUTTON, self.on_elimina)
        lista_sizer.Add(self.btn_elimina, 0, wx.ALIGN_TOP)

        main_sizer.Add(lista_sizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        panel.SetSizer(main_sizer)
        self.txt_nome.SetFocus()
        self.Centre()

    # ------------------------------------------------------------------------
    # Validazione
    # ------------------------------------------------------------------------
    def _valida(self):
        nome = self.txt_nome.GetValue().strip()
        cognome = self.txt_cognome.GetValue().strip()
        telefono = self.txt_telefono.GetValue().strip()

        if not nome:
            return None, "Il campo 'Nome' è obbligatorio."
        if not self._RE_TESTO.match(nome):
            return None, "Il 'Nome' può contenere solo lettere, spazi, apostrofi e trattini."
        if not cognome:
            return None, "Il campo 'Cognome' è obbligatorio."
        if not self._RE_TESTO.match(cognome):
            return None, "Il 'Cognome' può contenere solo lettere, spazi, apostrofi e trattini."
        if not telefono:
            return None, "Il campo 'Telefono' è obbligatorio."
        if not re.match(r"^\+?[0-9 \-().]+$", telefono):
            return None, ("Il telefono può contenere solo cifre, spazi, trattini, "
                          "parentesi ed eventualmente un '+' iniziale.")
        if not (6 <= len(re.sub(r"\D", "", telefono)) <= 15):
            return None, "Il numero di telefono deve contenere tra 6 e 15 cifre."

        return {"nome": nome, "cognome": cognome, "telefono": telefono}, None

    # ------------------------------------------------------------------------
    # Eventi
    # ------------------------------------------------------------------------
    def on_aggiungi(self, event):
        contatto, errore = self._valida()
        if errore:
            wx.MessageBox(errore, "Dati non validi", wx.OK | wx.ICON_WARNING)
            return

        # 1) aggiorna il MODELLO
        cid = self._next_id
        self._next_id += 1
        self._contatti[cid] = contatto

        # 2) aggiorna la VISTA, legando la riga alla chiave del dizionario
        index = self.lista.InsertItem(self.lista.GetItemCount(), contatto["nome"])
        self.lista.SetItem(index, 1, contatto["cognome"])
        self.lista.SetItem(index, 2, contatto["telefono"])
        self.lista.SetItemData(index, cid)      # riga -> chiave nel dizionario

        # 3) pulizia campi
        self.txt_nome.Clear()
        self.txt_cognome.Clear()
        self.txt_telefono.Clear()
        self.txt_nome.SetFocus()

    def on_elimina(self, event):
        sel = self.lista.GetFirstSelected()
        if sel == -1:
            wx.MessageBox("Seleziona prima una riga da eliminare.",
                          "Nessuna selezione", wx.OK | wx.ICON_INFORMATION)
            return

        cid = self.lista.GetItemData(sel)   # ricava la chiave dalla riga
        self._contatti.pop(cid, None)       # rimuovi dal MODELLO
        self.lista.DeleteItem(sel)          # rimuovi dalla VISTA

    # ------------------------------------------------------------------------
    # Esempio: ora i dati sono nel modello, non nelle celle.
    # ------------------------------------------------------------------------
    def get_contatti(self):
        """Restituisce la lista dei contatti correnti (dal modello)."""
        return list(self._contatti.values())


def main():
    app = wx.App(False)
    frame = RubricaFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()