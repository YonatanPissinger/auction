from flask import Flask, request
from protobuf_out import messages
from database import Database
import betterproto
import http

PORT = 80
SERVER = "127.0.0.1"
app = Flask("Server Name")

database = Database.Database()


@app.route('/', methods=['POST'])
def parse_request(self=None):
    received_data: bytes = request.data
    try:
        received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
        received_message.FromString(received_data)
        received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
        typename = received_messages[0]
        if typename == "new_user_data":
            try:
                data: messages.NewUserData() = received_message.new_user_data

                SignUpCheckDetails(data)

                message_to_user = messages.MessageToUser()
                message_to_user.success = messages.ServerSuccess()
                message_to_user.success.success_message = "SignUp Successfully"
                return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "old_user_data":
            try:
                data: messages.OldUserData() = received_message.old_user_data

                SignInCheckDetails(data)

                # message_to_user = messages.MessageToUser()
                # message_to_user.full_user_data = messages.NewUserData()
                # message_to_user.full_user_data = SignInCheckDetails(data)

                # return bytes(message_to_user.full_user_data), http.HTTPStatus.OK

                message_to_user = messages.MessageToUser()
                message_to_user.success = messages.ServerSuccess()
                message_to_user.success.success_message = "SignIn Successfully"
                return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "customer_product_data":
            try:
                data: messages.CustomerProductData() = received_message.customer_product_data

                AddNewProduct(data)

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
                data: messages.SellerProductData() = received_message.seller_product_data

                FindMatch(data)

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


@app.route('/', methods=['POST'])
def SendFullUserData():
    pass
    # TODO: send full user data


def SignUpCheckDetails(user_data: messages.NewUserData()):
    exist = 0
    users_tuple = database.UsersListToTuple()
    for user in users_tuple:
        if user_data.user_name == user.user_name:
            exist = exist + 1
    if exist > 0:
        print("user name is not available")
    else:
        print("user name is available")
        database.AddUser(user_data)

    print(users_tuple)


def SignInCheckDetails(user_data: messages.OldUserData()):
    exist = 0
    users_tuple = database.UsersListToTuple()
    for user in users_tuple:
        if user_data.user_name == user.user_name and user_data.user_name == user.user_name:
            print("user name and password are correct")
            exist = exist + 1
            return user
    if exist == 0:
        print("user name or password are incorrect")

    print(users_tuple)


def AddNewProduct(customer_product: messages.CustomerProductData()):
    database.AddProduct(customer_product)


def FindMatch(seller_product: messages.SellerProductData):
    products_tuple = database.ProductListToTuple()
    for product in products_tuple:
        if product.customer_product_type == seller_product.seller_product_type:
            database.AddMatchingProduct(product)
    messages.ListRelevantCustomerData = database.RelevantProductsToSellerListToTuple()


if __name__ == '__main__':
    app.run(SERVER, PORT, debug=True)
