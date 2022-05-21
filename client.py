# import socket

# IP = socket.gethostbyname(socket.gethostname())
# PORT = 4456
# ADDR = (IP, PORT)
# FORMAT = "utf-8"
# SIZE = 1024

# def main():
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(ADDR)

#     while True:
#         data = client.recv(SIZE).decode(FORMAT)
#         cmd, msg = data.split("@")

#         if cmd == "DISCONNECTED":
#             print(f"[SERVER]: {msg}")
#             break
#         elif cmd == "OK":
#             print(f"{msg}")

#         data = input("> ")
#         data = data.split(" ")
#         cmd = data[0]

#         if cmd == "HELP":
#             client.send(cmd.encode(FORMAT))
#         elif cmd == "LOGOUT":
#             client.send(cmd.encode(FORMAT))
#             break
#         elif cmd == "LIST":
#             client.send(cmd.encode(FORMAT))
#         elif cmd == "DELETE":
#             client.send(f"{cmd}@{data[1]}".encode(FORMAT))
#         elif cmd == "UPLOAD":
#             path = data[1]

#             with open(f"{path}", "r") as f:
#                 text = f.read()

#             filename = path.split("/")[-1]
#             send_data = f"{cmd}@{filename}@{text}"
#             client.send(send_data.encode(FORMAT))

#     print("Disconnected from the server.")
#     client.close()

# if __name__ == "__main__":
#     main()

import socket

class Client:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 4455
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = "utf-8"
        self.SIZE = 1024
         
    
    def run(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(self.ADDR)

        data = client.recv(self.SIZE).decode(self.FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            return 
        elif cmd == "OK":
            print(f"{msg}")

        path = "client_data/index.html"
        with open(f"{path}", "r") as f:
            text = f.read()
        filename = path.split("/")[-1]
        send_data = f"{filename}@{text}"
        client.send(send_data.encode(self.FORMAT))
        output = client.recv(self.SIZE).decode(self.FORMAT)
        output = output.split("@")
        if output[0] == "OK":
            print(output[1])
        else: print("There was a problem uploading your file to the server, retrying....")



