import wx
from mna import OpenScreen, CustomerScreen, SellerRequestScreen
from protobuf_out import messages
import requests
import betterproto
from flask import Flask, request


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


def GetUserName() -> messages.PreviousProductsRequest:

    user_name = messages.PreviousProductsRequest()
    user_name.previous_products_user_name_request = customer_name

    return user_name


class SecondScreen(CustomerScreen):
    def __init__(self):
        super().__init__(None)

    def GetCustomerProductData(self) -> messages.CustomerProductData:
        customer_product_data = messages.CustomerProductData()
        customer_product_data.user_name = customer_name
        customer_product_data.user_phone_number = customer_phone_number
        customer_product_data.customer_product_type = self.ProductTypeBox.GetValue()
        customer_product_data.customer_note = self.NoteBox.GetValue()
        return customer_product_data

    def AddButtonOnButtonClick(self, event):
        customer_data = self.GetCustomerProductData()
        QueryServerForCustomerProduct(customer_data)

    def DownloadedButton_OnButtonClick(self, event):
        user_name = GetUserName()
        QueryServerForPreviousProductRequest(user_name, self)


class ThirdScreen(SellerRequestScreen):
    def __init__(self):
        super().__init__(None)

    def GetSellerProductData(self) -> messages.SellerProductData:
        seller_product_data = messages.SellerProductData()
        seller_product_data.seller_product_type = self.ProductTypeBox_Seller.GetValue()

        return seller_product_data

    def matchButtonOnButtonClick(self, event):
        QueryServerForSellerProduct(self.GetSellerProductData(), self)


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

    if typename == "server_success":
        print("פרטי רישום נשלחו לשרת בהצלחה")
        wx.MessageBox("רישום בוצע בהצלחה!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
        CustomerOrSeller(new_user_data)
    elif typename == "user_is_exist":
        print("שם משתמש תפוס")
        wx.MessageBox("שם המשתמש שהזנת תפוס, נסה שם אחר", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def QueryServerForOldUser(old_user_data: messages.OldUserData):
    message_to_server = messages.MessageToServer()
    message_to_server.old_user_data = old_user_data
    data_to_server: bytes = message_to_server.SerializeToString()
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")

    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    typename = received_messages[0]

    if typename == "full_user_data":
        full_user_data = received_messages[1]
        print("פרטי התחברות נשלחו לשרת בהצלחה")
        wx.MessageBox("אתה מוכר לנו!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
        CustomerOrSeller(full_user_data)
    elif typename == "incorrect_user_details":
        print("שגיאת התחברות")
        wx.MessageBox("שם המשתמש או הסיסמה שהזנת שגויים!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def QueryServerForCustomerProduct(customer_product_data: messages.CustomerProductData):
    message_to_server = messages.MessageToServer()
    message_to_server.customer_product_data = customer_product_data
    data_to_server: bytes = message_to_server.SerializeToString()
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")

    typename = received_messages[0]
    if typename == "server_success":
        print("מוצר הועלה בהצלחה")
        wx.MessageBox("בקשת המוצר נרשמה בהצלחה!", "Popup Message", wx.OK | wx.ICON_INFORMATION)
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def QueryServerForSellerProduct(seller_product_data: messages.SellerProductData, self=None):
    message_to_server = messages.MessageToServer()
    message_to_server.seller_product_data = seller_product_data
    data_to_server: bytes = message_to_server.SerializeToString()
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")

    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    message_to_user.match_products.FromString(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    sizer = wx.BoxSizer(wx.VERTICAL)

    typename = received_messages[0]
    if typename == "match_products":
        if self is not None:

            for product in received_messages[1].relevant_match_products:
                # Create a StaticText control for each product and add it to the sizer
                text = wx.StaticText(self.m_scrolledWindow3,
                                     label=f"name: {product.user_name}; note: {product.customer_note}; phone: {product.user_phone_number}")
                sizer.Add(text, 0, wx.ALL, 5)  # Add each StaticText control to the sizer with some spacing

            # Set the sizer for the scrolled window
            self.m_scrolledWindow3.SetSizer(sizer)

            # Fit the sizer to the scrolled window's size
            sizer.Fit(self.m_scrolledWindow3)
        print(received_messages[1])
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "":
        print(f"Server returned success: {message_to_user.match_products.relevant_match_products}")
        pass
    else:
        raise RuntimeError(f"Unexpected message from server: {typename}")


def QueryServerForPreviousProductRequest(customer_name_request: messages.PreviousProductsRequest, self=None):
    message_to_server = messages.MessageToServer()
    message_to_server.previous_products = customer_name_request
    data_to_server: bytes = message_to_server.SerializeToString()
    res = requests.post("http://127.0.0.1:80/",
                        data=data_to_server,
                        headers={'Content-Type': 'application/octet-stream'})

    if res.status_code != requests.codes.ok:
        raise Exception(f"Server returned status code {res.status_code}")
    message_to_user: messages.MessageToUser = messages.MessageToUser().parse(res.content)
    received_messages = betterproto.which_one_of(message_to_user, "StructMessageToUser")
    sizer = wx.BoxSizer(wx.VERTICAL)

    typename = received_messages[0]
    if typename == "current_customer_products":
        if self is not None:

            for product in received_messages[1].relevant_current_customer_products:
                # Create a StaticText control for each product and add it to the sizer
                text = wx.StaticText(self.m_scrolledWindow2,
                                     label=f"type: {product.customer_product_type}; note: {product.customer_note}")
                sizer.Add(text, 0, wx.ALL, 5)  # Add each StaticText control to the sizer with some spacing

            # Set the sizer for the scrolled window
            self.m_scrolledWindow2.SetSizer(sizer)

            # Fit the sizer to the scrolled window's size
            sizer.Fit(self.m_scrolledWindow2)

        print(received_messages[1])
    elif typename == "server_error":
        error_message: str = message_to_user.server_error.error_message
        raise RuntimeError(error_message)
    elif typename == "":
        print(f"Server returned success: {message_to_user.match_products.relevant_match_products}")
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
