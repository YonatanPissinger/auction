import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.decode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

if __name__ == "__main__":
    print("[STARTING] Server is starting...")




