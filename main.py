import wx
from mna import OpenScreen, CustomerScreen, SellerScreen
from protobuf_out import messages
import requests
import betterproto
from database import Database

users = Database.Database()


def QueryServerForNewUser(user_data: messages.UserData):
    message_to_server = messages.MessageToServer()
    message_to_server.user_data = user_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})


def QueryServerForOldUser(old_user_data: messages.OldUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.old_user_data = old_user_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})


def QueryServerForCustomer(data_from_customer: messages.CustomerProductData):
    message_to_server = messages.MessageToServer()
    message_to_server.customer_product_data = data_from_customer
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


def QueryServerForSeller(data_from_seller: messages.SellerProductData):
    # HTTP POST request to server using "requests" library
    message_to_server = messages.MessageToServer()
    message_to_server.seller_product_data = data_from_seller
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    # Check status code
    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    # Parse response from server as messages.MessageToSeller
    message_to_seller: messages.MessageToSeller = messages.MessageToSeller().parse(res.content)
    # Check if server returned ServerError or RelevantList using "betterproto.which_one_of"
    received_messages = betterproto.which_one_of(message_to_seller, "StructMessageToSeller")
    typename = received_messages[1]
    if typename == "server_error":
        error_message: str = message_to_seller.server_error.error_message
        # Throw exception with error message
        raise RuntimeError(error_message)
    elif typename == "ListRelevantCustomerData":
        print(f"Server returned success: {message_to_seller.list_relevant_customer_data.relevant_customers}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


class FirstScreen(OpenScreen):
    def __init__(self):
        super().__init__(None)

    def GetNewUserData(self) -> messages.UserData:

        user_data = messages.UserData()
        user_data.user_name = self.UserNameBox.GetValue()
        user_data.password = self.PasswordBox.GetValue()
        user_data.phone_number = self.PhoneBox.GetValue()
        if self.CustomerButton:
            user_data.status = "Customer"
        else:
            user_data.status = "Seller"

        return user_data

    def GetOldUserData(self) -> messages.OldUserData:

        old_user_data = messages.OldUserData()
        old_user_data.user_name = self.UserNameBoxOfSubscriber.GetValue()
        old_user_data.password = self.PasswordBoxOfSubscriber.GetValue()

        return old_user_data

    def EnterButtonOnButtonClick(self, event):
        if self.Enter.AddPage(self.SignIn, u"הרשם", True):
            QueryServerForNewUser(self.GetNewUserData())
        else:
            QueryServerForOldUser(self.GetOldUserData())


class SecondScreen(CustomerScreen):
    def __init__(self):
        super().__init__(None)

    def GetCustomerData(self) -> messages.CustomerProductData:
        firstScreen = FirstScreen()
        customer_data = messages.CustomerProductData()
        customer_data.product = self.ProductTypeBox.GetValue()
        customer_data.note = self.NoteBox.GetValue()
        customer_data.customer_name = firstScreen.UserNameBox.GetValue()
        customer_data.customer_number = firstScreen.PhoneBox.GetValue()

        return customer_data

    def AddButtonOnButtonClick(self, event):
        customer_data = self.GetCustomerData()
        QueryServerForCustomer(customer_data)
        wx.MessageBox("Your product uploaded successfully!", "Success", wx.OK | wx.ICON_INFORMATION)


class ThirdScreen(SellerScreen):
    def __init__(self):
        super().__init__(None)

    def GetSellerData(self) -> messages.SellerProductData:
        seller_data = messages.SellerProductData()
        seller_data.product = self.ProductTypeBox_Seller.GetValue()
        return seller_data

    def matchButtonOnButtonClick(self, event):
        seller_data = self.GetSellerData()
        QueryServerForSeller(seller_data)


if __name__ == '__main__':
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
