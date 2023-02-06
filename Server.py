from flask import Flask, request
from protobuf_out import messages
from database import Database
import betterproto
import http
import wx
from main import FirstScreen, SecondScreen, ThirdScreen, ForthScreen

PORT = 80
SERVER = "127.0.0.1"
app = Flask("Server Name")

database: Database = Database.Database()

users = database.UsersListToTuple()
products = database.ProductListToTuple()


@app.route('/', methods=['POST'])
def parse_request(self=None):
    received_data: bytes = request.data
    try:
        received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
        received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
        typename = received_messages[0]
        if typename == "new_user_data":
            try:
                print(1)
                # check if this username used
                SignUpCheckDetails(self.received_message.user_data)

                message_to_user = messages.MessageToUser()
                message_to_user.success = messages.ServerSuccess()
                message_to_user.success.success_message = ""
                return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "old_user_data":
            try:
                print(2)
                # check if this username exist
                SignInCheckDetails(self.received_message.old_user_data)

                message_to_user = messages.MessageToUser()
                message_to_user.success = messages.ServerSuccess()
                message_to_user.success.success_message = ""
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "customer_product_data":
            try:
                print(3)
                # add product
                AddNewProduct(received_message.customer_product_data)

                message_to_user = messages.MessageToUser()
                message_to_user.success = messages.ServerSuccess()
                message_to_user.success.success_message = ""
                return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "seller_product_data":
            try:
                print(4)
                # check matching
                MatchChecking(received_message.seller_product_data)

                message_to_user = messages.MessageToUser()
                message_to_user.list_relevant_customer_data = messages.ListRelevantCustomerData()
                return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        else:
            raise Exception(f"Unidentified message type received: {typename}")
    except Exception as e:
        return str(e), http.HTTPStatus.OK


def SignUpCheckDetails(user_data: messages.NewUserData()):
    exist = 0
    for user in users:
        if user_data.NewUserNameBox.GetValue() == user.user_name:
            exist = exist + 1
    if exist > 0:
        wx.MessageBox("שם המשתמש שהזנת תפוס")
        user_data.UserNameBox.clear()
    else:
        database.AddUser(user_data.GetNewUserData())
    print(users)


def SignInCheckDetails(user_data: messages.OldUserData()):
    exist = 0
    for user in users:
        if user_data.OldUserNameBox.GetValue() == user.user_name and user_data.OldUserPasswordBox:
            exist = 1
    if exist == 0:
        wx.MessageBox("שם המשתמש או הסיסמה שהזנת שגויים")
        user_data.UserNameBoxOfSubscriber.clear()
        user_data.PasswordBoxOfSubscriber.clear()
    print(users)


def AddNewProduct(customer_product: messages.CustomerProductData()):
    database.AddProduct(customer_product)


def MatchChecking(seller_product: messages.SellerProductData):
    for product in products:
        if product.customer_product_type == seller_product.seller_product_type:
            pass
        else:
            wx.MessageBox("לא נמצאו התאמות למוצר שברשותך")


app.run(SERVER, PORT, debug=True)
