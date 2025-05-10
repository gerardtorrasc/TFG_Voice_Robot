import socket

# Configuració client
HOST = '127.0.0.1'  # IP del servidor (canviar la ip a la que toqui)
PORT = 65432        # El mateix port que el servidor

# Crear socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'1')   # Enviem el dígit 1 com a byte
    print("Dígit enviat: 1")