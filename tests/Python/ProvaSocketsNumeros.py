import socket

# Configuració
HOST = "84.88.129.201"  # IP del robot
PORT = 2002             # Port del socket voice_server

print("Iniciant client de proves amb bucle")
print("0: Entrar")
print("1: Sortir")
print("2: Pivotar+")
print("3: Pivotar-")
print("4: Tornar a home")
print("5: Tancar connexió")

while True:
    ordre = input("Introdueix una comanda (0–5): ").strip()

    if ordre == "5":
        print("Finalitzant comunicació.")
        break

    if ordre not in ["0", "1", "2", "3", "4", "5"]:
        print("Comanda no vàlida. Introdueix 0, 1, 2, 3, 4 o 5.")
        continue

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(ordre.encode("utf-8"))
            print(f"Comanda enviada: {ordre}")
    except Exception as e:
        print(f"Error en enviar: {e}")
