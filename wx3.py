import wx

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="Event Example", size=(400, 300))

        panel = wx.Panel(self)

        button = wx.Button(panel, label="Click Me", pos=(120, 100))

        button.Bind(wx.EVT_BUTTON, self.on_click)

        self.Show()

    def on_click(self, event):
        wx.MessageBox("Button clicked!")

app = wx.App()
frame = MyFrame()
app.MainLoop()