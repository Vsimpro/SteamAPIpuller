#! python3 server-threading.py

import os
import socket
import commandline
from scraper import print_database
import threading
           

# Global variables
header = 64 
port = 1337
format = "utf-8"
dc_msg = "!disconnect"
recv_msg = "!received"
backlog = []

hostname = (socket.gethostbyname_ex(socket.gethostname())[2][2])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (hostname, port)
server.bind(addr)

def handle_client(connection, address):
    print(f"[New Connection] {address} connected")
    connected = True
    while connected:
        msg_length = connection.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(format)
            if msg == dc_msg:
                connected = False
                print("[Client disconnected.]")
            else:
                backlog = f"[{address}]: {msg}\n"
                print(backlog)
                connection.send(recv_msg.encode(format))
                with open("remote_log.txt", "a", encoding="utf-8") as file:
                    file.write(backlog)
                commandline.main(msg)
    connection.close()

def stop():
    os._exit()

def main():
    print("Hold your horses!")
    print(f"[Server] host {hostname} starting...")
    server.listen()
    print("[Server] open on hostname.")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[Active threads] {threading.activeCount() - 2}")


if __name__ == "__main__":
    main()

