import socket
import pickle


if __name__ == '__main__':
    sock = socket.socket()

    with open("addr.txt", "r") as file:
        for address in file.readlines():
            sock.connect((address, 9090))
            sock.send(bytes("OK", "utf-8"))
            data = sock.recv(1024)
            print(bytes.decode(data, "utf-8"))
