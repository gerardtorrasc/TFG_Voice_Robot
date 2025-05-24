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
### 1. Part Robòtica:
- Instal·lar **Stäubli Robotics Suite (SRS)**
- Descarregar l'arxiu .zip que podeu trobar a la carpeta `the_voice_robot_project` dins d'aquest repositori
### 2. Part Python (reconeixement de veu)
- Instal·lar Python
- Instal·lar un intèrpret de Python (per exemple: Visual Studio Code)
- Obrir un terminal i executar:
    ```bash
    pip install SpeechRecognition
    pip install pyaudio
    ```
  > Nota: si `pyaudio` dona error, pots instal·lar un fitxer `.whl` manual.
### Manual Complet
Podeu consultar el manual d'instal·lació complet i amb instruccions detallades la carpeta `docs` d'aquest repositori

## Manual d'usuari


## Autoria
Gerard Torras Canela

Grau en Enginyeria Biomèdica

Universitat de Girona

Curs 2024–2025

**Tutor**: Xavier Cufí Solé

**Suport docent addicional**: Professor Esteve-Amadeu Hernandez Uptegrove


## Llicència
Aquest projecte es publica sota la llicència MIT, permetent-ne l’ús, modificació i distribució amb reconeixement d’autoria.
