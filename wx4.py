import wx

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="Input Example", size=(400, 300))

        panel = wx.Panel(self)

        self.text = wx.TextCtrl(panel, pos=(100, 50), size=(200, 30))

        button = wx.Button(panel, label="Show Text", pos=(120, 120))

        button.Bind(wx.EVT_BUTTON, self.show_text)

        self.Show()

    def show_text(self, event):
        value = self.text.GetValue()

        wx.MessageBox(f"You typed: {value}")

app = wx.App()
frame = MyFrame()
app.MainLoop()