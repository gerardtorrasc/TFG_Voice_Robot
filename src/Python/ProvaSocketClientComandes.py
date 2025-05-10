import socket

HOST = '192.168.1.150'  # IP del PC servidor o 127.0.0.1 si ho proves local
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connectat al servidor!")

    while True:
        print("\nIntrodueix una comanda:")
        print("- I;<distància>; per entrar")
        print("- O;<distància>; per sortir")
        print("- L;<graus>; per pivotar a l'esquerra")
        print("- R;<graus>; per pivotar a la dreta")
        print("(Exemple: I;10;)")
        
        msg = input(">>> ").strip()
        
        if msg:
            if msg[-1] != ';':
                msg += ';'  # Afegeix el ; final si falta
            s.sendall(msg.encode('utf-8'))

