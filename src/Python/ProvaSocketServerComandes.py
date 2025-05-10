import socket

HOST = '192.168.1.147'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f" Servidor escoltant a {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Connectat per {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8').strip()

            mode = msg[0]  # Primer caràcter
            value_part = msg[2:-1]  # El número entre ';'

            try:
                valor = int(value_part)
            except ValueError:
                print("Error: Valor no vàlid.")
                continue

            if mode == 'I':
                print(f"Entrant {valor} cm.")
            elif mode == 'O':
                print(f"Sortint {valor} cm.")
            elif mode == 'L':
                print(f"Pivotant a l'esquerra {valor} graus.")
            elif mode == 'R':
                print(f"Pivotant a la dreta {valor} graus.")
            else:
                print(f"Ordre desconeguda: {mode}")

