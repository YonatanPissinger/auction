from flask import Flask, request
from protobuf_out import messages
import betterproto
import http

PORT = 80
SERVER = "127.0.0.1"

app = Flask("Server Name")


@app.route('/', methods=['POST'])
def parse_request():
    received_data: bytes = request.data
    try:
        received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
        received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
        typename = received_messages[0]
        if typename == "customer_data":
            return "", http.HTTPStatus.OK
        elif typename == "seller_data":
            raise Exception("Too many sellers, help!")
            message_to_seller = messages.ListCustomerData()
            customer = messages.CustomerData()
            customer.product = "Red horse"
            message_to_seller.customers.append(customer)
            return bytes(message_to_seller), http.HTTPStatus.OK
        else:
            raise Exception(f"Unidentified type {typename}")
    except Exception as e:
        server_error = messages.ServerError()
        server_error.error_message = str(e)
        return bytes(server_error), http.HTTPStatus.OK


app.run(SERVER, PORT, debug=True)
