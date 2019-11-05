import os
import socket
import platform


def save_inf():
    # Information about the system
    info = '\n'.join(["OS name: " + os.name,
                      "System: " + platform.system(),
                      "Release: " + platform.release(),
                      "Network name: " + platform.node(),
                      "Version: " + platform.version(),
                      "Processor: " + platform.processor()])

    # Create socket to send data
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 9090))
    sock.listen(1)

    # Handle connection to send data
    while True:
        conn, addr = sock.accept()
        print("connected")

        data = conn.recv(1024)
        if not data:
            continue

        conn.send(bytes(info, "utf-8"))
        conn.close()


if __name__ == '__main__':
    save_inf()
