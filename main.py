import wx
from mna import OpenScreen, CustomerScreen, SellerRequestScreen, SellerResultScreen
from protobuf_out import messages
import requests
import betterproto


check_customer_or_seller_status: str = ""
check_new_or_old_user: str = ""

customer_name: str = ""
customer_phone_number: str = ""


class FirstScreen(OpenScreen):
    def __init__(self):
        super().__init__(None)

    def EnterButtonOnButtonClick(self, event):
        check = self.EnterOnNotebookPageChanged(event)
        if check == "new":
            new_user_data = self.GetNewUserData()
            QueryServerForNewUser(new_user_data)
        elif check == "old":
            old_user_data = self.GetOldUserData()
            QueryServerForOldUser(old_user_data)

    def EnterOnNotebookPageChanged(self, event):
        global check_new_or_old_user
        if self.Enter.GetSelection() == 0:
            check_new_or_old_user = "old"
        elif self.Enter.GetSelection() == 1:
            check_new_or_old_user = "new"
        return check_new_or_old_user

    def GetNewUserData(self) -> messages.NewUserData:

        new_user_data = messages.NewUserData()
        new_user_data.user_name = self.NewUserNameBox.GetValue()

        global customer_name
        customer_name = self.NewUserNameBox.GetValue()

        new_user_data.user_password = self.NewUserPasswordBox.GetValue()
        new_user_data.user_phone_number = self.NewUserPhoneBox.GetValue()

        global customer_phone_number
        customer_phone_number = self.NewUserPhoneBox.GetValue()

        new_user_data.user_status = check_customer_or_seller_status

        return new_user_data

    def GetOldUserData(self) -> messages.OldUserData:

        old_user_data = messages.OldUserData()
        old_user_data.user_name = self.OldUserNameBox.GetValue()

        global customer_name
        customer_name = self.OldUserNameBox.GetValue()

        old_user_data.user_password = self.OldUserPasswordBox.GetValue()

        return old_user_data

    def CustomerButtonOnRadioButton(self, event):
        global check_customer_or_seller_status
        check_customer_or_seller_status = "customer"

    def SellerButtonOnRadioButton(self, event):
        global check_customer_or_seller_status
        check_customer_or_seller_status = "seller"


class SecondScreen(CustomerScreen):
    def __init__(self):
        super().__init__(None)

    def GetCustomerProductData(self) -> messages.CustomerProductData:

        customer_product_data = messages.CustomerProductData()
        customer_product_data.user_name = customer_name
        customer_product_data.user_phone_number = customer_phone_number
        customer_product_data.product = self.ProductTypeBox.GetValue()
        customer_product_data.note = self.NoteBox.GetValue()

        return customer_product_data

    def AddButtonOnButtonClick(self, event):
        customer_data = self.GetCustomerProductData()
        QueryServerForCustomerProduct(customer_data)


class ThirdScreen(SellerRequestScreen):
    def __init__(self):
        super().__init__(None)

    def GetSellerProductData(self) -> messages.SellerProductData:
        seller_product_data = messages.SellerProductData()
        seller_product_data.product = self.ProductTypeBox_Seller.GetValue()

        return seller_product_data

    def matchButtonOnButtonClick(self, event):
        QueryServerForSellerProduct(self.GetSellerProductData())
        forth_screen = ForthScreen()
        forth_screen.Show()


class ForthScreen(SellerResultScreen):
    def __init__(self):
        super().__init__(None)


def QueryServerForNewUser(new_user_data: messages.NewUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.new_user_data = new_user_data
    data_to_server: bytes = message_to_server.SerializeToString()
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")

    typename = received_messages[0]
    if typename == "success":
        print("פרטי רישום נשלחו לשרת בהצלחה")
        wx.MessageBox("רישום בוצע בהצלחה!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "ListRelevantCustomerData":
        print(f"Server returned success: {message_to_user.list_relevant_customer_data.relevant_customers}")
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")

    CustomerOrSeller(new_user_data)


def QueryServerForOldUser(old_user_data: messages.OldUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.old_user_data = old_user_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    typename = received_messages[0]
    if typename == "full_user_data":
        print("פרטי התחברות נשלחו לשרת בהצלחה")
        wx.MessageBox("אתה מוכר לנו!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "success":
        print("פרטי התחברות נשלחו לשרת בהצלחה")
        wx.MessageBox("אתה מוכר לנו!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "ListRelevantCustomerData":
        print(f"Server returned success: {message_to_user.list_relevant_customer_data.relevant_customers}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")

    # CustomerOrSeller(full_user_data)


def QueryServerForCustomerProduct(customer_product_data: messages.CustomerProductData):
    message_to_server = messages.MessageToServer()
    message_to_server.customer_product_data = customer_product_data
    data_to_server = bytes(message_to_server)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    print(res.status_code)

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    typename = received_messages[0]
    if typename == "success":
        print("מוצר הועלה בהצלחה")
        wx.MessageBox("מוצר הועלה בהצלחה!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
        pass
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "ListRelevantCustomerData":
        print(f"Server returned success: {message_to_user.list_relevant_customer_data.relevant_customers}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def QueryServerForSellerProduct(seller_product_data: messages.SellerProductData):
    message_to_user = messages.MessageToUser()
    message_to_user.seller_product_data = seller_product_data
    data_to_server = bytes(message_to_user)
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})
    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    typename = received_messages[0]
    if typename == "success":
        print("מוצר נשלח לבדיקת התאמה בהצלחה")
    if typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "ListRelevantCustomerData":
        print(f"Server returned success: {message_to_user.list_relevant_customer_data.relevant_customers}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def CustomerOrSeller(user_data: messages.NewUserData):

    second_screen = SecondScreen()
    third_screen = ThirdScreen()
    if user_data.user_status == "customer":
        second_screen.Show()
    elif user_data.user_status == "seller":
        third_screen.Show()


if __name__ == '__main__':
    app = wx.App()
    window = FirstScreen()
    window.Show()
    app.MainLoop()
