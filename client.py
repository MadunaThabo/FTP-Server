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



