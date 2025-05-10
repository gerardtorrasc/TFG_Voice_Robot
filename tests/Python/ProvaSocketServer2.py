import socket

HOST = '192.168.1.150'  # Escoltar a qualsevol IP local
PORT = 5000       # Port triat (igual al client)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f" Servidor escoltant a {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f" Connectat per {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Si es tanca la connexió
            msg = data.decode('utf-8').strip()

            if msg == "S":
                print("Ordre rebuda: Iniciar moviment.")
            elif msg == "E":
                print("Ordre rebuda: Aturar moviment.")
            elif msg.startswith("A"):
                try:
                    dist = int(msg[1:])  # Extreu número després de la 'A'
                    print(f" Avançant {dist} cm.")
                except ValueError:
                    print("Error: Distància no vàlida.")
            else:
                print(f" Ordre desconeguda: {msg}")
