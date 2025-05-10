import socket

# Configuració servidor
HOST = '192.168.1.147'  # IP local (proves a la mateixa màquina)
PORT = 65432        # Port arbitrari lliure (>1024)

# Crear socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f" Servidor escoltant a {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f" Connectat per {addr}")
        data = conn.recv(1024)
        if data:
            print(f" Rebut: {data.decode('utf-8')}")