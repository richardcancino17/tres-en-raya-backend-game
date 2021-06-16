# tres-en-raya
A project made in Python using the framework Django 2.0.8

TRES EN RAYA 

Es un juego típico y común en muchos lugares del mundo.
Para jugar al tres en raya necesitarás un tablero de 3x3. El juego trata de ir marcando los espacios del tablero alternadamente hasta que uno de los jugadores consiga hacer tres en raya.

Lenguaje: Python 3.6
Framework: Django 2.0

¿Cómo jugar? - Listado de Endpoints

* /api/v0.1/player/register  ===> Registrar a un usuario
- - Fields: email: EmailField, password: CharField (está encriptado), username: CharField

* /api/v0.1/player/login/mobile/<backend> ====> Registrar o Login mediante Facebook
- - Aquí, deberias cambiar '<backend>' por 'facebook' y en el field 'access_token', deberías colocar el token que te genera Facebook (https://developers.facebook.com/tools/explorer/)

*  /api/v0.1/player/login ====> Login de un usuaio
- - Fields: email: EmailField, password: CharField (está encriptado)

* /api/v0.1/players ====> Lista de jugadores
- - Fields: id: IntegerField, username: CharField

* /api/v0.1/games/create ====> Crear un juego
- - Fields: player_2: IntegerField (Colocar el id del player 2)

* /api/v0.1/games/ ====> Lista de juegos

* /api/v0.1/games/<id_game> ====> Detalle de un juego en específico

* /api/v0.1/games/<id_game>/moves ====> Fase de movimientos de un juego
- - Fields: player: PrimaryKeyRelatedField, position: IntegerField

El juego se termina cuando realizas un tres en raya y automáticamente cambia de estado a 'done'.

¡Éxitos y que gane el mejor!
