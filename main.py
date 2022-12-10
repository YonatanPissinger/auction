import wx
from mna import OpenScreen, SellerOrCustomer, CustomerScreen, SellerScreen, SuccessScreen
from protobuf_out import messages
import requests
import betterproto


def QueryServer(data_from_customer: messages.CustomerData):
    # HTTP POST request to server using "requests" library
    message_to_server = messages.MessageToServer()
    message_to_server.customer_data = data_from_customer
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    # Check status code
    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    # Parse response from server as messages.MessageToCustomer
    message_to_customer: messages.MessageToCustomer = messages.MessageToCustomer().parse(res.content)
    # Check if server returned ServerError or EmptyMessage using "betterproto.which_one_of"
    received_messages = betterproto.which_one_of(message_to_customer, "StructMessageToCustomer")
    typename = received_messages[0]
    if typename == "server_error":
        error_message: str = message_to_customer.server_error.error_message
        # Throw exception with error message
        raise RuntimeError(error_message)
    elif typename == "success":
        print(f"Server returned success: {message_to_customer.success.additional_information}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


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
        QueryServer(customer_data)
        # Tell user that success has occurred
        wx.MessageBox("Success!", "Success", wx.OK | wx.ICON_INFORMATION)
        self.SuccessScreenToCustomer()

    def GetCustomerData(self) -> messages.CustomerData:
        customer_data = messages.CustomerData()
        customer_data.product = self.TypeBox.GetValue()
        customer_data.note = self.ComentsBox.GetValue()
        customer_data.customer_name = self.NameBox.GetValue()
        customer_data.customer_number = self.PhoneBox.GetValue()

        return customer_data



    @staticmethod
    def fidbekToCustomer(answer) -> messages.MessageToCustomer:
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
        seller_data = self.GetSellerData()
        QueryServer(seller_data)

    def GetSellerData(self) -> messages.SellerData:
        seller_data = messages.SellerData()
        seller_data.product = self.ProductBox.GetValue()
        return seller_data


class FifthScreen(SuccessScreen):
    def __init__(self):
        super().__init__(None)


if '__main__' == __name__:
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
