import socket

HOST = '192.168.1.150'  # Escoltar a qualsevol IP local
PORT = 5000       # Port triat

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escoltant a {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Connectat per {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8').strip()

            mode = msg[0]  # Primer caràcter
            try:
                value = int(msg[2:-1])  # Número entre ';'
            except:
                value = 0

            if mode == 'I':
                print(f"Entrant {value} cm.")
            elif mode == 'O':
                print(f"Sortint {value} cm.")
            elif mode == 'L':
                print(f"Pivotant {value} graus esquerra.")
            elif mode == 'R':
                print(f"Pivotant {value} graus dreta.")
            else:
                print(f"Ordre desconeguda: {msg}")
