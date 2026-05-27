import wx

app = wx.App()

frame = wx.Frame(None, title="Buttons Example", size=(400, 300))

panel = wx.Panel(frame)

button = wx.Button(panel, label="Click Me", pos=(120, 100))

frame.Show()

app.MainLoop()