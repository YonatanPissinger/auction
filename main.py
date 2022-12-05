import wx
from mna import OpenScreen, SellerOrCustomer

if '__main__' == __name__:
    pass


class FirstScreen(OpenScreen):
    def __init__(self):
        super().__init__()

    def EnterOnButtonClick(self, event):
        open(SecondScreen)


class SecondScreen(SellerOrCustomer):
    def __init__(self):
        super().__init__()





app = wx.App()
window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
window.Show(True)
app.MainLoop()
