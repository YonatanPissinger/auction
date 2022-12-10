import requests
import wx
from mna import OpenScreen, SellerOrCustomer, CustomerScreen, SellerScreen, SuccessScreen
from protobuf_out import messages

from protobuf_out.messages import MessageToServer
from flask import Flask, request


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
        self.QueryServer(customer_data)
        self.SuccessScreenToCustomer()

    def GetCustomerData(self) -> messages.CustomerData:
        customer_data = messages.CustomerData()
        customer_data.product = self.TypeBox.GetValue()
        customer_data.note = self.ComentsBox.GetValue()
        customer_data.customer_name = self.NameBox.GetValue()
        customer_data.customer_number = self.PhoneBox.GetValue()

        return customer_data

    @staticmethod
    def QueryServer(data_from_customer: messages.CustomerData):

        res = requests.post("http://127.0.0.1:80/",
                            data=bytes(data_from_customer),
                            headers={'Content-Type': 'application/octet-stream'})

    @staticmethod
    def fidbeKToCustomer(answer) -> messages.MessageToCustomer:
        fidbek_to_customer = answer
        return fidbek_to_customer

    def SuccessScreenToCustomer(self):
        fifth_screen = FirstScreen()
        fifth_screen.Show()
        self.Close()


class FourthScreen(SellerScreen):
    def __init__(self):
        super().__init__(None)

    def matchButtonOnButtonClick(self, event):
        seller_data = messages.SellerData()
        seller_data.product = self.ProductName.GetValue()

        print(seller_data)


class FifthScreen(SuccessScreen):
    def __init__(self):
        super().__init__(None)


if '__main__' == __name__:
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
