import socket

def client_program():
    host = socket.gethostname()
    port = 12000
    
    clientSocket = socket.socket()
    clientSocket.connect((host,port))
    
    message = input("->")
    
    while message.lower().strip() != 'quit':
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
        
        print('Server: ' + data)
        message = input('->')
        
    clientSocket.close()

if __name__ == '__main__':
    client_program()