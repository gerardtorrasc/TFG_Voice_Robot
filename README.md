# TFG_Voice_Robot
Aquest projecte de Treball de Fi de Grau consisteix en el desenvolupament d’un sistema que permet controlar un braç robòtic Stäubli TX60 mitjançant comandes de veu, amb aplicació específica a un entorn quirúrgic simulat de laparoscòpia.

El sistema transforma la veu en ordres estructurades, que es transmeten via sockets TCP/IP fins a un receptor que les interpreta i activa els moviments del robot. Els moviments controlats estan dissenyats per simular l’entrada i sortida de la càmera pel trocar i la pivotació al voltant del punt d’inserció, tal com es requereix en procediments laparoscòpics.

## Estructura del repositori
- `docs/`: Memòria, manuals d'usuari i instal·lació i fitxer amb els requeriments
- `src/`: Codis finals del sistema integrat
- `tests/`: Scripts de proves parcials (veu, sockets, moviment)
- `the_voice_robot_project`: Carpeta amb l'arxiu `Voice_Robot.zip`. El fitxer `Voice_Robot.zip` conté el projecte final creat a l'entorn SRS19, preparat per ser obert directament al simulador o a la consola MCP del robot.
- `LICENSE`: Llicència MIT que regula l’ús i distribució del projecte
- `README.md`: aquest fitxer



## Requeriments
- **Python**
- **Llibreries Python**:
  - `speech_recognition`
  - `pyaudio`
  - `socket`
  - `re`
- **Hardware i entorn**
  - Micròfon USB o ordinador amb micròfon integrat
  - **Robot Stäubli TX60** amb connexió TCP/IP activa
  - **Consola MCP** per controlar i supervisar el robot
  - **Ordinador amb el software SRS19 instal·lat**, per executar i simular programes en llenguatge VAL3
  - **Intèrpret i entorn de desenvolupament Python**, com Visual Studio Code, PyCharm o similar
- **Sistema operatiu**: Windows o Linux


## Instal·lació
### 1. Part Robòtica (SRS):
- Instal·lar **Stäubli Robotics Suite (SRS)** des de la web oficial
- Descarregar l'arxiu `.zip` que podeu trobar a la carpeta `the_voice_robot_project` dins d'aquest repositori
  
### 2. Part Python (reconeixement de veu)
- Instal·lar Python
- Instal·lar un entorn de desenvolupament com **Visual Studio Code** o utilitzar la terminal
- Obrir un terminal i executar:
    ```bash
    pip install SpeechRecognition
    pip install pyaudio
    ```
  > Nota: si `pyaudio` dona error, pots instal·lar un fitxer `.whl` manual.

### Manual Complet
Podeu consultar el manual d'instal·lació complet i amb instruccions detallades la carpeta `docs` d'aquest repositori

## Manual d'usuari
### 1. Preparació del sistema
- Encén el robot i prepara'l per la simulació (afageix l'eina, el pacient, etc.)
- Assegura't que treballes amb un ordinador connectat a la mateixa xarxa que el robot
- Encén el micròfon i comprova que funciona

### 2. Llançament del sitema 
- Descomprimeix el zip del projecte
- Obre SRS i carrega el projecte
- Envia el programa al robot a partir del gestor de transferència. No oblideu seleccionar el mode de funcionament mitjançant la variable verbose
- Des de la consola del robot, obre la aplicació i executa-la amb el botó de RUN
- Un cop la aplicació està funcionant en el robot, obre el Visual Studio Code o un terminal i executa el fitxer `socketVoice.py`

### 3. Ús del sistema
- Quan el sistema estigui actiu i el robot s'hagi mogut fins a fer la inserció al pacient, dona ordres com:
  - "entra" → Mou el braç cap a dins.

  - "surt" → Mou el braç cap a fora.

  - "dreta" → Pivota a la dreta del pacient.

  - "esquerra" → Pivota a l'esquerra.

  - "casa" o "torna" → Torna a la posició HOME.

  - "final" → Tanca la connexió.

### 4. Finalització
- Un cop finalitzat l'ús (s'envii la ordre de tornar a la posició HOME), el robot tornarà a home automàticament
- Pots aturar el codi de python dient la ordre "final" o "fi" i s'acabarà l'execució

### Manual Complet
Podeu consultar el manual d'usuari complet i amb instruccions detallades la carpeta `docs` d'aquest repositori


## Autoria
Gerard Torras Canela

Grau en Enginyeria Biomèdica

Universitat de Girona

Curs 2024–2025

**Tutor**: Xavier Cufí Solé

**Suport docent addicional**: Professor Esteve-Amadeu Hernandez Uptegrove


## Llicència
Aquest projecte es publica sota la llicència MIT, permetent-ne l’ús, modificació i distribució amb reconeixement d’autoria.
