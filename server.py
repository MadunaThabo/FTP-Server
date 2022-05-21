
import os
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))

    while True:
        #get data
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        name, text = data[0], data[1]
        filepath = os.path.join(SERVER_DATA_PATH, name)
        #making or editing file
        with open(filepath, "w+") as f:
            f.truncate(0)
            f.write(text)

        send_data = "OK@File uploaded successfully."
        conn.send(send_data.encode(FORMAT))
        break
    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        print("http://localhost/test/test/server_data/index.html")
        
if __name__ == "__main__":
    main()
