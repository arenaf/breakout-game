# Breakout Game

![banner_breakout](https://github.com/arenaf/breakout-game/assets/169451601/8f48107c-5765-409d-8403-61c0cdf872d8)

## Sobre el desarrollo

Éste juego se desarrolló con ***Python*** y se utilizó el módulo ***Turtle*** como interfaz gráfica.

### Archivos contenidos
- Un archivo principal **main.py**: desde donde se debe ejecutar el programa. Se encarga de controlar que se inicie la pantalla y no se cierre hasta que el ususario pulse el botón de *cerrar*. También llama a las funciones correspondientes de los siguientes módulos.
- Módulo **ball.py**: en este módulo se crea la bola y se controla su movimiento, rebotando en la pala, en un bloque o en la pared. Si el usuario sube de nivel, se encarga de incrementar la velocidad de la bola, a mayor nivel, mayor velocidad.
- Módulo **paddle.py**: su misión es crear la pala o plataforma (de color azul) y controlar la dirección hacia donde el usuario quiere que vaya. Hay dos posibilidades: izquierda o derecha.
- Módulo **scoreboard.py**: contiene la clase que actualiza la puntuación y el nivel. Guarda en un archivo el nivel más alto al que haya llegado el usuario y lo mantiene hasta que vuelva a haber nuevo récord.
- Archivo **data.txt**: éste es el fichero creado por el módulo definido anteriormente (**scoreboard.py**). En él se almacena el nivel más alto que se haya alcanzado. Si el archivo no existe, la clase se encarga de crearlo tras ejecutar el programa.

## Cómo se juega

Tras iniciar el juego se muestra una plataforma, una bola y un muro de ladrillos de varios colores. La bola empieza a moverse hacia la parte inferior de la pantalla.


![init-game](https://github.com/arenaf/breakout-game/assets/169451601/c925b8f2-87c8-41c4-9cd7-e9ca45645b5d)


El jugador es el encargado de controlar la plataforma (color azul), para ello debe usar las flechas del teclado izquierda y derecha. Su misión es impedir que la bola caiga al suelo y, a su vez, intentar que vaya hacia los ladrillos. 
Cuando la bola toca algún ladrillo, éste desaparece de pantalla.

![level1](https://github.com/arenaf/breakout-game/assets/169451601/770a9655-5272-4fe9-a569-36d50eba4683)


Si el jugador consigue sacar todos los ladrillos de la pantalla, se pasa al siguiente nivel. Cuanto mayor sea el nivel, la bola irá más rápido.

Si la bola cae al suelo, el jugador pierde y se acaba la partida.


![game-over](https://github.com/arenaf/breakout-game/assets/169451601/40b40dea-e051-4627-b476-8c50ec58e045)


