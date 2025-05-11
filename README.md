# TFG_Voice_Robot
Aquest projecte de Treball de Fi de Grau consisteix en el desenvolupament d’un sistema que permet controlar un braç robòtic Stäubli TX60 mitjançant comandes de veu, amb aplicació específica a un entorn quirúrgic simulat de laparoscòpia.

El sistema transforma la veu en ordres estructurades, que es transmeten via sockets TCP/IP fins a un receptor que les interpreta i activa els moviments del robot. Els moviments controlats estan dissenyats per simular l’entrada i sortida de la càmera pel trocar i la pivotació al voltant del punt d’inserció, tal com es requereix en procediments laparoscòpics.

##Estructura del repositori
- src/ : Codis finals del sistema integrat
- tests/ : Scripts de proves parcials (veu, sockets, moviment)
- docs/ : Memòria, manual d'usuari i instal·lació i fitxer amb els requeriments
- README.md : aquest fitxer


## Requeriments
- **Python**
- 
