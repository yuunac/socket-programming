#Server TCP che riceve la stringa da un client e fornisce il numero di vocali presenti nella stringa
from socket import *

#inserisco i parametri principali 
serverPort = 12200
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('Il server è pronto ad ascoltare (CTRL+C per terminare)')

while 1:
    count_vowels = 0
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(f'Il server ha ricevuto la stringa {sentence}')
    for char in sentence:
        if char in bytes('aeiou', 'utf-8'):
            count_vowels+=1
    connectionSocket.send(bytes(str(count_vowels), 'utf-8'))
    
connectionSocket.close()
    




