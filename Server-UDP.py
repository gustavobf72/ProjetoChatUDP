import socket

clientes = []

def main():

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    HOST = socket.gethostbyname(socket.gethostname()) 
    PORT = 5000
    orig = (HOST, PORT)
    try:
        udp.bind(orig)
    except:
        return print("Não deu certo, que pena")

    while True:
        cliente, addr = udp.recvfrom(1024)
        print("Conectado ao ", addr)
        clientes.append(cliente)

def gerencmsg(cliente):
    while True:
        try:
            msg = cliente.recvfrom(1024)
            transmicao(msg, cliente)
        except:
            excluircliente(cliente)
            break
 
def transmicao(msg, cliente):
    for numcliente in clientes:
        if numcliente != cliente:
            try:
                numcliente.sendto(msg)
            except:
                excluircliente(cliente)

def excluircliente(cliente):
    clientes.remove(cliente)


main()
