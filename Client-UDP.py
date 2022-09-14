from base64 import encode
import socket
import string

def main():
    HOST = '192.168.1.6' # Endereco IP do Servidor
    PORT = 5000 # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    print ('\n...Para sair digite <bye>...\n')
    
    print("Digite hello para conectar")
    
    while True:
        conec = input("--> ")
    
        if conec != 'hello':    
            print("Digitação errada, digite hello para continuar!")
        else:
            username = input('Usuário-> ')
            udp.sendto(username.encode(), dest)
            print('\nConectado')
            break

    print("\nDigite <inscrever> para entrar na lista\n")
    while True:
        passw = input("--> ")
        if passw != 'inscrever':
            print("Palavra errada! Digite a palavra inscrever para entrar na lista!")
            
        else:
            print("Parabéns, você entrou na lista!")
            break

    print("\nDigite <desinscrever> para sair da lista\n")
    while True:
        passw = input("--> ")
        if passw != 'desinscrever':
            print("Palavra errada! Digite a palavra desinscrever para sair da lista!")
            
        else:
            print("Parabéns você saiu da lista!")
            break
    
    while True:
         enviarmsg(udp, username)   

def recebermsg (udp):
    while True:
        try: 
            
            msg = udp.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            udp.close()
            print("\n Obrigado! volte sempre.")
            break

def enviarmsg (udp, username):
    while True:
        try:          
                msg = input("\n")
                if msg != 'bye':
                    msg = udp.sendto(f'<{username}> {msg}'.encode('utf-8'))
                else:
                    udp.close()
                    break
        except:
            return
main()
