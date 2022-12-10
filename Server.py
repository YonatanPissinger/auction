from flask import Flask, request
from protobuf_out import messages
import betterproto
import http

PORT = 80
SERVER = "127.0.0.1"
app = Flask("Server Name")


@app.route('/', methods=['POST'])
def parse_request():
    Server.parse_request()


class Server:

    @staticmethod
    def parse_request():
        received_data: bytes = request.data
        try:
            received_message: messages.MessageToServer = messages.MessageToServer().parse(received_data)
            received_messages = betterproto.which_one_of(received_message, "StructMessageToServer")
            typename = received_messages[0]
            if typename == "seller_data":
                try:
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
                    database = Database()
                    list_of_customers = database.customer_requests
                    list_of_customers.append()
                    message_to_customer = messages.MessageToCustomer()
                    message_to_customer.success = messages.EmptyMessage()
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

    app.run(SERVER, PORT, debug=True)


class Database(messages.MessageToServer):
    def __init__(self):
        super().__init__()
        self.customer_requests = None
        self._customer_requests: [messages.CustomerData] = []

    @property
    def get_customer_requests(self):
        return self._customer_requests
