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

                if SignUpCheckDetails(data):
                    message_to_user = messages.MessageToUser()
                    message_to_user.server_success = messages.ServerSuccess()
                    message_to_user.server_success.success_message = ""
                    return bytes(message_to_user), http.HTTPStatus.OK
                else:
                    message_to_user = messages.MessageToUser()
                    message_to_user.user_is_exist = messages.SignUpProblem()
                    message_to_user.user_is_exist.user_name_exist = True
                    return bytes(message_to_user), http.HTTPStatus.OK
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "old_user_data":
            try:
                data: messages.OldUserData() = received_message.old_user_data

                if SignInCheckDetails(data):
                    full_user_data: messages.NewUserData() = GefFullUserData(data)

                    message_to_user = messages.MessageToUser()
                    message_to_user.full_user_data = messages.NewUserData()
                    message_to_user.full_user_data = full_user_data
                    return bytes(message_to_user), http.HTTPStatus.OK
                else:
                    message_to_user = messages.MessageToUser()
                    message_to_user.incorrect_user_details = messages.SignInProblem()
                    message_to_user.incorrect_user_details.user_name_or_password_incorrect = True
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
                message_to_user.server_success = messages.ServerSuccess()
                message_to_user.server_success.success_message = ""
                return bytes(message_to_user), http.HTTPStatus.OK

                # list_of_customer: messages.ListCurrentCustomerProducts() = FindCustomerProduct(data)

                # message_to_user = messages.MessageToUser()
                # message_to_user.current_customer_products = messages.ListCurrentCustomerProducts()
                # message_to_user.current_customer_products = list_of_customer
                # return bytes(message_to_user), http.HTTPStatus.OK
                # WHY IS CONTINUE HERE????
            # equal to the full user data that sent

            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "seller_product_data":
            try:
                data: messages.SellerProductData() = received_message.seller_product_data

                if MatchFound(data):
                    list_of_matching = FindMatch(data)

                    actually_list = list(list_of_matching)

                    message_to_user = messages.MessageToUser()
                    message_to_user.match_products = messages.ListMatchProducts()
                    message_to_user.match_products = actually_list
                    return bytes(message_to_user), http.HTTPStatus.OK
                else:
                    message_to_user = messages.MessageToUser()
                    message_to_user.there_is_not_match_product = messages.MatchWasNotFound()
                    message_to_user.there_is_not_match_product = True
            except Exception as e:
                message_to_user = messages.MessageToUser()
                message_to_user.server_error = messages.ServerError()
                message_to_user.server_error.error_message = str(e)
                return bytes(message_to_user), http.HTTPStatus.OK
        elif typename == "previous_products":
            try:
                data: messages.PreviousProductsRequest() = received_message.previous_products

                list_of_customer: messages.ListCurrentCustomerProducts() = FindCustomerProduct(data)

                actually_list = list(list_of_customer)

                message_to_user = messages.MessageToUser()
                message_to_user.current_customer_products = messages.ListCurrentCustomerProducts()
                message_to_user.current_customer_products = actually_list
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
def SignUpCheckDetails(user_data: messages.NewUserData()):
    user_not_exist = True
    users_tuple = database.UsersListToTuple()
    for user in users_tuple:
        if user_data.user_name == user.user_name:
            user_not_exist = False
    if user_not_exist:
        print("user name is available")
        database.AddUser(user_data)
    else:
        print("user name is not available")
    return user_not_exist


def SignInCheckDetails(user_data: messages.OldUserData()):
    user_exist = False
    users_tuple = database.UsersListToTuple()
    for user in users_tuple:
        if user.user_name == user_data.user_name and user.user_password == user_data.user_password:
            user_exist = True
    if user_exist:
        print("user name and password are correct")
    else:
        print("user name or password are incorrect")
    return user_exist


def GefFullUserData(partial_user_data: messages.OldUserData):
    users_tuple = database.UsersListToTuple()
    for user in users_tuple:
        if user.user_name == partial_user_data.user_name and user.user_password == partial_user_data.user_password:
            full_user_data = user
            return full_user_data


def AddNewProduct(customer_product: messages.CustomerProductData()):
    database.AddProduct(customer_product)


def MatchFound(seller_product: messages.SellerProductData):
    products_tuple = database.ProductListToTuple()
    found = False
    for product in products_tuple:
        if product.customer_product_type == seller_product.seller_product_type:
            found = True
            return found
    return found


def FindMatch(seller_product: messages.SellerProductData):
    products_tuple = database.ProductListToTuple()
    for product in products_tuple:
        if product.customer_product_type == seller_product.seller_product_type:
            database.AddMatchingProduct(product)
    products_tuple = database.RelevantProductsToSellerListToTuple()
    return products_tuple


def FindCustomerProduct(customer_name: messages.CustomerProductData.user_name):
    products_tuple = database.ProductListToTuple()
    for product in products_tuple:
        if product.user_name == customer_name.previous_products_user_name_request:
            database.AddCurrentCustomerProduct(product)
    customer_products_tuple = database.RelevantProductsOfCustomerListToTuple()

    return customer_products_tuple


if __name__ == '__main__':
    app.run(SERVER, PORT, debug=True)
