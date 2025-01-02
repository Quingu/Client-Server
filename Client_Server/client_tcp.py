import socket  #Cria conecções que ajuda a ouvir as portas

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Family , type  (stream = tcp)
client.settimeout(1)
ip = "127.0.0.1"
porta = 456
try:
    client.connect(ip, porta)
    client.send(b"Teste") # Aqui irá a mensagem, caso use uma solicitação http a chamada será: GET / HTTP/1.1\nHost:ip
    pacote_recebido = client.recv(1024).decode()#recebe a resposta
    print(pacote_recebido)
except Exception as e:
    print("Ocorreu um erro", e)