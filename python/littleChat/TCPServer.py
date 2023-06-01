import socket
from datetime import date

def server_program():
    #get the hostname
    host = socket.gethostname()
    port = 12000
    
    serverSocket = socket.socket()
    serverSocket.bind((host, port))
    
    serverSocket.listen(1)
    print('In attesa della connessione con un client')
    connectionSocket,addr = serverSocket.accept()
    print("Avviata la connessione con: " + str(addr))
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        
        if data == 'ciao':
            data = 'Ciao anche a te!'
            connectionSocket.send(data.encode())
        elif data.find('come stai')!=-1:
            data = 'Io sto bene!Spero che anche tu stia bene'
            connectionSocket.send(data.encode())
        elif data.find('squadra preferita')!=-1:
            data = 'La mia squadra preferita è l\'Inter'
            connectionSocket.send(data.encode())
        elif data.find('piatto preferito')!=-1:
            data = 'Il mio piatto preferito è la pizza'
            connectionSocket.send(data.encode())
        elif data.find('giorno'):
            today = str(date.today())
            data = 'Oggi è il ' + today
            connectionSocket.send(data.encode())
        elif(data.find('grazie'))!=-1:
            data = 'Figurati! Nessun problema'
            connectionSocket.send(data.encode())
        
    connectionSocket.close()
    
if __name__ == '__main__':
    server_program()