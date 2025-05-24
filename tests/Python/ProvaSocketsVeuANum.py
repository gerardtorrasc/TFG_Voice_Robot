import socket
import speech_recognition as sr

HOST = "84.88.129.201"  # IP del robot
PORT = 2002             # Port del robot

def escolta_ordre():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Esperant comanda de veu...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ca-ES").lower()
        print(f"Has dit: {text}")
        return text
    except sr.UnknownValueError:
        print("No s'ha entès la comanda.")
        return None
    except sr.RequestError as e:
        print(f"Error amb el servei de reconeixement: {e}")
        return None

def veu_a_ordre(text):
    if text is None:
        return None
    if "entra" in text:
        return "0"
    if "surt" in text:
        return "1"
    if "esquerra" in text:
        return "2"
    if "dreta" in text:
        return "3"
    if "casa" in text or "torna" in text:
        return "4"
    if "fi" in text or "final" in text:
        return "5"
    return None
    


print("Client de veu iniciat. Digues 'final' o 'fi' per acabar.")

while True:
    text = escolta_ordre()
    ordre = veu_a_ordre(text)

    if ordre is None:
        print("Ordre no reconeguda.")
        continue

    if ordre == "5":
        print("Finalitzant comunicació.")
        break

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(ordre.encode("utf-8"))
            print(f"Comanda enviada: {ordre}")
    except Exception as e:
        print(f"Error en enviar: {e}")
