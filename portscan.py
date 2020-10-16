import socket
import sys

argumentos = sys.argv

try:
    dominio = argumentos[1]
    alt = argumentos[2]
except:
    print("Faltam argumentos no programa")
    sys.exit(1)

portas = [80, 8080, 443, 21, 25, 23]

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex((dominio, porta))
    if codigo == 0:
        print("{} OPEN".format(porta))
    elif alt == 'n':
        print("{} CLOSE".format(porta))
    else: 
       continue



