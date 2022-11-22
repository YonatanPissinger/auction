import socket

from messages_pb2 import customer_data



HEADER = 2048
PORT = 5013
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

new_customer = customer_data()

sendd = new_customer.SerialliazeToString()


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


if __name__ == "__main__":
    send(sendd)
    send(DISCONNECT_MESSAGE)
