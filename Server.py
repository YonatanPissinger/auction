from flask import Flask, request
from protobuf_out import messages
from database import Database
import betterproto
import http

PORT = 80
SERVER = "0.0.0.0"
app = Flask("Server Name")

customers_database = Database.Database()


@app.route('/', methods=['POST'])
def parse_request():
    # TODO: Remove this line
    print("Got message!")
    received_data: bytes = request.data
    try:
        received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
        received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
        typename = received_messages[0]
        if typename == "seller_data":
            try:
                MatchChecking(received_message.seller_data)
                message_to_seller = messages.MessageToSeller()
                message_to_seller.list_customer_data = messages.ListCustomerData()
                customer = messages.CustomerData()
                customer.product = "Red horse"
                message_to_seller.list_customer_data.customers.append(customer)
                return bytes(message_to_seller), http.HTTPStatus.OK
            except Exception as e:
                message_to_seller = messages.MessageToSeller()
                message_to_seller.server_error = messages.ServerError()
                message_to_seller.server_error.error_message = str(e)
                return bytes(message_to_seller), http.HTTPStatus.OK
        elif typename == "customer_data":
            try:
                customers_database.add_customer_request(received_message.customer_data)
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


def MatchChecking(seller_data):
    for customer in customers_database.customer_requests():
        if customer.product == messages.SellerData.product:
            print("Match found")
        else:
            print("No match found")


app.run(SERVER, PORT, debug=True)
