import wx
from mna import OpenScreen, SellerOrCustomer, CustomerScreen, SellerScreen
from protobuf_out import messages


class FirstScreen(OpenScreen):
    def __init__(self):
        super().__init__(None)

    def EnterOnButtonClick(self, event):
        second_screen = SecondScreen()
        second_screen.Show()
        self.Close()


class SecondScreen(SellerOrCustomer):
    def __init__(self):
        super().__init__(None)

    def CustomerOnClick(self, event):
        third_screen = ThirdScreen()
        third_screen.Show()
        self.Close()

    def SellerOnClick(self, event):
        fourth_screen = FourthScreen()
        fourth_screen.Show()
        self.Close()


class ThirdScreen(CustomerScreen):
    def __init__(self):
        super().__init__(None)

    def AddButtonOnButtonClick(self, event):
        customer_data = self.GetCustomerData()


    def GetCustomerData(self) -> messages.CustomerData:
        customer_data = messages.CustomerData()
        customer_data.product = self.TypeBox.GetValue()
        customer_data.note = self.ComentBox.GetValue()
        customer_data.customer_name = self.NameBox.GetValue()
        customer_data.customer_number = int(self.PhoneBox.GetValue(), 10)

        return customer_data

    def QueryServer(self, data):



class FourthScreen(SellerScreen):
    def __init__(self):
        super().__init__(None)

    def matchButtonOnButtonClick( self, event ):
        seller_data = messages.SellerData()
        seller_data.product = self.ProductName.GetValue()


if '__main__' == __name__:
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
