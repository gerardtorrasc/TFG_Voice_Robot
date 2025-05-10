import socket

HOST = '192.168.1.150'  # Canvia-ho per la IP real del servidor
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        msg = input("Introdueix comanda (S/E/A20): ").strip()
        if msg:
            s.sendall(msg.encode('utf-8'))
