# TFG_Voice_Robot
Aquest projecte de Treball de Fi de Grau consisteix en el desenvolupament d’un sistema que permet controlar un braç robòtic Stäubli TX60 mitjançant comandes de veu, amb aplicació específica a un entorn quirúrgic simulat de laparoscòpia.

El sistema transforma la veu en ordres estructurades, que es transmeten via sockets TCP/IP fins a un receptor que les interpreta i activa els moviments del robot. Els moviments controlats estan dissenyats per simular l’entrada i sortida de la càmera pel trocar i la pivotació al voltant del punt d’inserció, tal com es requereix en procediments laparoscòpics.

## Estructura del repositori
- `src/`: Codis finals del sistema integrat
- `tests/`: Scripts de proves parcials (veu, sockets, moviment)
- `docs/`: Memòria, manuals d'usuari i instal·lació i fitxer amb els requeriments
- `README.md`: aquest fitxer
- `the_voice_robot_project`: Carpeta amb l'arxiu `Voice_Robot.zip`. El fitxer `Voice_Robot.zip` conté el projecte final creat a l'entorn SRS19, preparat per ser obert directament al simulador o a la consola MCP del robot.


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
