#client TCP che prende in input una stringa e restituisce il numero di vocali presenti in essa

from socket import *
serverName = 'localhost'
serverPort = 12200

clientSocket = socket(AF_INET,SOCK_STREAM) #indica che la connessione è di tipo TCP
clientSocket.connect((serverName,serverPort)) #cerca di connettersi a quel server utilizzando quella porta

sentence = bytes(input('Inserisci una stringa e ti dirò il numero di vocali presenti al suo interno (CTRL+C per terminare)'), 'utf-8') #dati di input
clientSocket.send(sentence)
count_vowels = clientSocket.recv(1024)
print(f'Il numero di vocali contate dal server è {count_vowels}')
clientSocket.close()
