import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 150))
        panel = wx.Panel(self)
        
        button1 = wx.Button(panel, label="Button 1", pos=(10, 10))
        button2 = wx.Button(panel, label="Button 2", pos=(10, 40))
        button3 = wx.Button(panel, label="Button 3", pos=(10, 70))

        button1.Bind(wx.EVT_BUTTON, self.on_button1_click)
        button2.Bind(wx.EVT_BUTTON, self.on_button2_click)
        button3.Bind(wx.EVT_BUTTON, self.on_button3_click)

    def on_button1_click(self, event):
        wx.MessageBox("Button 1 clicked!", "Button 1")

    def on_button2_click(self, event):
        wx.MessageBox("Button 2 clicked!", "Button 2")

    def on_button3_click(self, event):
        wx.MessageBox("Button 3 clicked!", "Button 3")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "wxPython Button Example")
    frame.Show()
    app.MainLoop()
