import re  # Llibreria per treballar amb expressions regulars
import speech_recognition as sr  # Llibreria per reconeixement de veu

# Diccionari per convertir paraules numèriques en nombres
text_to_number = {
    "zero": 0, "u": 1, "un": 1, "una": 1, "dos": 2, "dues": 2,
    "tres": 3, "quatre": 4, "cinc": 5, "sis": 6, "set": 7,
    "vuit": 8, "nou": 9, "deu": 10, "onze": 11, "dotze": 12,
    "tretze": 13, "catorze": 14, "quinze": 15, "setze": 16,
    "disset": 17, "divuit": 18, "dinou": 19, "vint": 20, 
    "vint-i-u": 21, "vint-i-dos": 22, "vint-i-tres": 23
}

def convertir_paraules_a_numeros(text):
    """
    Converteix paraules numèriques en nombres. Exemple:
    "baixa cinc centímetres" -> "baixa 5 centímetres"
    """
    words = text.split()  # Divideix el text en paraules separades
    result = []
    for word in words:
        if word in text_to_number:  # Si la paraula està al diccionari, la substitueix
            result.append(str(text_to_number[word]))
        else:
            result.append(word)  # Si no està al diccionari, manté la paraula
    return " ".join(result)  # Retorna el text amb els números convertits

# Inicialitzar el reconeixedor de veu
recognizer = sr.Recognizer()

with sr.Microphone() as source:  # Obrim el micròfon per escoltar
    print("Escoltant (en català)...")
    audio = recognizer.listen(source)  # Guarda l'àudio capturat

try:
    # Convertir àudio a text utilitzant Google Speech-to-Text
    text = recognizer.recognize_google(audio, language="ca-ES")
    print(f"Ordre reconeguda: {text}")

    # Convertir les paraules numèriques a nombres
    text_numeric = convertir_paraules_a_numeros(text)
    print(f"Text convertit: {text_numeric}")

    # Expressió regular per detectar ordres de moviment amb diferents formes
    match = re.search(r"(baixa|puja|mou|avança)\s+(\d+)\s*(centímetres|cm)?", text_numeric)

    if match:
        accio = match.group(1)  # Primer grup: l'acció (baixa, puja, mou, avança)
        distancia = int(match.group(2))  # Segon grup: el número reconegut
        unitat = match.group(3) if match.group(3) else "centímetres"  # Si no s'especifica "cm", assumeix "centímetres"

        print(f"Acció detectada: {accio}")
        print(f"Distància detectada: {distancia} {unitat}")
    else:
        print("No s'ha trobat cap ordre reconeguda.")  # Si l'ordre no segueix el patró esperat

# Control d'errors per millorar la robustesa del programa
except sr.UnknownValueError:
    print("No s'ha pogut entendre l'àudio. Intenta parlar més clar.")  # No s'ha entès la veu
except sr.RequestError:
    print("Error amb el servei de reconeixement de veu.")  # Problema amb la connexió al servei de Google
except Exception as e:
    print(f"Error inesperat: {e}")  # Qualsevol altre error inesperat
