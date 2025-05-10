import socket
import speech_recognition as sr

HOST = '192.168.1.139'  # IP del servidor
PORT = 5000

# Configura reconeixedor de veu
r = sr.Recognizer()

def escolta_ordre():
    with sr.Microphone() as source:
        print("Escoltant...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ca-ES")
        print(f"Ordre reconeguda: {text}")
        return text.lower()
    except Exception as e:
        print(f"Error reconeixent veu: {e}")
        return None

# Connexió socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connectat al servidor!")

    while True:
        ordre = escolta_ordre()

        if ordre:
            # Traduïm l'ordre de veu a codi
            if "entra" in ordre:
                s.sendall(b"I;10;")   # Entrar 10 cm (exemple)
            elif "sortir" in ordre or "surt" in ordre:
                s.sendall(b"O;10;")   # Sortir 10 cm
            elif "esquerra" in ordre:
                s.sendall(b"L;15;")   # Pivotar esquerra 15 graus
            elif "dreta" in ordre:
                s.sendall(b"R;15;")   # Pivotar dreta 15 graus
            else:
                print("Ordre de veu no reconeguda.")

