import socket  #Cria conecções que ajuda a ouvir as portas

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Family , type  (dgram = udp)
client.settimeout(1)
ip = "127.0.0.1" #input("Digite o endereço: ")
porta = 456 #int(input("Digite a porta: "))
try:
    while True:
        msg = input("Mensagem: ") + "\n" 
        client.sendto((msg.encode()),(ip,porta))
        data, sender = client.recvfrom(1024)#recebe a resposta
        print(sender[0] + ":" + data.decode())
        if data.decode == "sair\n" or msg == "sair\n":
            break
    client.close()
except Exception as e:
    print("Ocorreu um erro", e)
    client.close()