import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

file = open("output.txt", "w")

try:
    server.bind("0.0.0.0", 456) #serve para estabelecer a "localização"
    server.listen(5)#serve para escutar a conexão
    print("Listening...")
    
    client_socket, address  = server.accept()#Espera a conexão
    print("Received from: " + address[0])
    
    data = client_socket.recv(1024).decode()
    
    file.write(data)
    """
    while TRUE:
        data = client_socket.recv(1024).decode()
        if data == senhasecreta\n:
            client_socket.send(b"mensagem secreta")
    """
    server.close()
except Exception as e:
    print("erro" , e)
    server.close()