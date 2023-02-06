import wx
from mna import OpenScreen, CustomerScreen, SellerRequestScreen, SellerResultScreen
from protobuf_out import messages
import requests
import betterproto


class FirstScreen(OpenScreen):
    def __init__(self):
        super().__init__(None)

    check_customer_or_seller_status: str = ""
    check_new_or_old_user: str = ""

    def EnterButtonOnButtonClick(self, event):
        self.UserButtonOnButtonClick(event)

    def CustomerButtonOnRadioButton(self, event):
        global check_customer_or_seller_status
        check_customer_or_seller_status = "customer"

    def SellerButtonOnRadioButton(self, event):
        global check_customer_or_seller_status
        check_customer_or_seller_status = "seller"

    def GetNewUserData(self) -> messages.NewUserData:

        new_user_data = messages.NewUserData()
        new_user_data.user_name = self.NewUserNameBox.GetValue()
        print(new_user_data.user_name)
        new_user_data.password = self.NewUserPasswordBox.GetValue()
        print(new_user_data.password)
        new_user_data.phone_number = self.NewUserPhoneBox.GetValue()
        print(new_user_data.phone_number)
        new_user_data.user_status = check_customer_or_seller_status
        print(new_user_data.user_status)

        return new_user_data

    def GetOldUserData(self) -> messages.OldUserData:

        old_user_data = messages.OldUserData()
        old_user_data.user_name = self.OldUserNameBox.GetValue()
        print(old_user_data.user_name)
        old_user_data.password = self.OldUserPasswordBox.GetValue()
        print(old_user_data.password)

        return old_user_data

    def EnterOnNotebookPageChanged(self, event):
        global check_new_or_old_user
        if self.Enter.GetSelection() == 0:
            check_new_or_old_user = "old"
        elif self.Enter.GetSelection() == 1:
            check_new_or_old_user = "new"
        return check_new_or_old_user

    def UserButtonOnButtonClick(self, event):
        check = self.EnterOnNotebookPageChanged(event)
        if check == "new":
            print("הרשם")
            new_user_data = self.GetNewUserData()
            QueryServerForNewUser(new_user_data)
            wx.MessageBox("Your account created successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
        elif check == "old":
            print("התחבר")
            old_user_data = self.GetOldUserData()
            QueryServerForOldUser(old_user_data)
            wx.MessageBox("Your account logged in successfully!", "Success", wx.OK | wx.ICON_INFORMATION)


class SecondScreen(CustomerScreen):
    def __init__(self):
        super().__init__(None)

    def GetCustomerData(self) -> messages.CustomerProductData:

        customer_product_data = messages.CustomerProductData()
        customer_product_data.product = self.ProductTypeBox.GetValue()
        customer_product_data.note = self.NoteBox.GetValue()

        return customer_product_data

    def AddButtonOnButtonClick(self, event):
        customer_data = self.GetCustomerData()
        QueryServerForCustomerProduct(customer_data)
        wx.MessageBox("Your product uploaded successfully!", "Success", wx.OK | wx.ICON_INFORMATION)


class ThirdScreen(SellerRequestScreen):
    def __init__(self):
        super().__init__(None)

    def GetSellerData(self) -> messages.SellerProductData:

        seller_product_data = messages.SellerProductData()
        seller_product_data.product = self.ProductTypeBox_Seller.GetValue()

        return seller_product_data

    def matchButtonOnButtonClick(self, event):
        QueryServerForSellerProduct(self.GetSellerData())
        forth_screen = ForthScreen()
        forth_screen.Show()


class ForthScreen(SellerResultScreen):
    def __init__(self):
        super().__init__(None)


def QueryServerForNewUser(new_user_data: messages.NewUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.new_user_data = new_user_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    print(res.status_code)


def QueryServerForOldUser(old_user_data: messages.OldUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.old_user_data = old_user_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    print(res.status_code)


def QueryServerForCustomerProduct(customer_product_data: messages.CustomerProductData):
    message_to_server = messages.MessageToServer()
    message_to_server.customer_product_data = customer_product_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    print(res.status_code)


def QueryServerForSellerProduct(seller_product_data: messages.SellerProductData):
    # HTTP POST request to server using "requests" library
    message_to_server = messages.MessageToServer()
    message_to_server.seller_product_data = seller_product_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    # Check status code
    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    # Parse response from server as messages.MessageToSeller
    message_to_seller: messages.MessageToUser = messages.MessageToUser().parse(res.content)
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




if __name__ == '__main__':
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
