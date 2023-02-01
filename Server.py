from flask import Flask, request
from protobuf_out import messages
from database import Database
import betterproto
import http
import wx

PORT = 80
SERVER = "0.0.0.0"
app = Flask("Server Name")

customers_database = Database.Database()
users = Database.Database()


@app.route('/', methods=['POST'])
def parse_request(self=None):
    received_data: bytes = request.data
    try:
        received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
        received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
        typename = received_messages[0]
        if typename == "user_data":
            try:
                SignUpCheckDetails(self.received_message.user_data)
                users.add_user(received_message.user_data)
                print(users.subscribers())
                message_to_customer = messages.MessageToCustomer()
                message_to_customer.success = messages.ServerSuccess()
                message_to_customer.success.success_message = ""
                return bytes(message_to_customer), http.HTTPStatus.OK
            except Exception as e:
                message_to_customer = messages.MessageToCustomer()
                message_to_customer.server_error = messages.ServerError()
                message_to_customer.server_error.error_message = str(e)
                return bytes(message_to_customer), http.HTTPStatus.OK

        elif typename == "old_user_data":
            try:

                SignInCheckDetails(self.received_message.old_user_data)
            except Exception as e:
                message_to_customer = messages.MessageToCustomer()
                message_to_customer.server_error = messages.ServerError()
                message_to_customer.server_error.error_message = str(e)
                return bytes(message_to_customer), http.HTTPStatus.OK

        elif typename == "seller_product_data":
            try:
                MatchChecking(received_message.seller_product_data)
                message_to_seller = messages.MessageToSeller()
                message_to_seller.list_relevant_customer_data = messages.ListRelevantCustomerData()
                return bytes(message_to_seller), http.HTTPStatus.OK
            except Exception as e:
                message_to_seller = messages.MessageToSeller()
                message_to_seller.server_error = messages.ServerError()
                message_to_seller.server_error.error_message = str(e)
                return bytes(message_to_seller), http.HTTPStatus.OK
        elif typename == "customer_product_data":
            try:
                customers_database.add_customer_request(received_message.customer_product_data)
                print(customers_database.customer_requests())
                message_to_customer = messages.MessageToCustomer()
                message_to_customer.success = messages.ServerSuccess()
                message_to_customer.success.success_message = ""
                return bytes(message_to_customer), http.HTTPStatus.OK
            except Exception as e:
                message_to_customer = messages.MessageToCustomer()
                message_to_customer.server_error = messages.ServerError()
                message_to_customer.server_error.error_message = str(e)
                return bytes(message_to_customer), http.HTTPStatus.OK
        else:
            raise Exception(f"Unidentified message type received: {typename}")
    except Exception as e:
        return str(e), http.HTTPStatus.OK


def MatchChecking(seller_product_data: messages.SellerProductData):
    print(customers_database.customer_requests())
    for customer in customers_database.customer_requests():
        if customer.product == messages.SellerProductData.product:
            print("Match found")
        else:
            print("No match found")


def CheckUserDetails(self):
    if self.Enter.AddPage(self.SignIn, u"הרשם", True):
        self.SignUpCheckDetails()
    else:
        self.SignInCheckDetails()


def SignUpCheckDetails(self):
    if self.UserNameBox.GetValue() not in users.subscribers():
        users.add_user(self.GetNewUserData())
    else:
        wx.MessageBox("שם המשתמש שהזנת תפוס")
        self.UserNameBox.clear()


def SignInCheckDetails(self):
    if self.UserNameBoxOfSubscriber.GetValue() in users.subscribers() and self.PasswordBoxOfSubscriber.GetValue() in users.subscribers():
        pass
    else:
        wx.MessageBox("שם המשתמש שהזנת לא קיים")
        self.UserNameBoxOfSubscriber.clear()
        self.PasswordBoxOfSubscriber.clear()


app.run(SERVER, PORT, debug=True)
