
# Space Invaders con Pygame

Este es un juego clásico de Space Invaders desarrollado en Python utilizando la biblioteca Pygame de manera simple. El jugador controla una nave espacial que debe eliminar a los alienígenas invasores antes de que lleguen a la parte inferior de la pantalla.

## Características del Juego
- Movimiento fluido de la nave con las teclas de dirección.
- Disparo de proyectiles con la tecla `ESPACIO`.
- Alienígenas que se mueven y descienden al tocar los bordes.
- Aumento de velocidad de los enemigos cada 5 puntos.
- Menú de selección de dificultad (Fácil, Medio y Difícil).
- Visualización del puntaje en pantalla.
- Fin del juego cuando un enemigo alcanza la nave.

## Instalación
Para ejecutar el juego, sigue estos pasos:

1. Asegúrate de tener Python instalado (versión 3.x recomendada).
2. Instala las dependencias necesarias ejecutando el siguiente comando:
   ```bash
   pip install pygame
   ```
3. Todas las imagenes necesarias estan en la carpeta `Imagenes` 
4. Ejecuta el script principal:
   ```bash
   python game.py
   ```

## Controles
- `FLECHA IZQUIERDA`: Mueve la nave a la izquierda.
- `FLECHA DERECHA`: Mueve la nave a la derecha.
- `ESPACIO`: Dispara proyectiles.

## Modos de Dificultad
El juego cuenta con tres niveles de dificultad seleccionables desde el menú inicial:
- **Fácil**: 8 enemigos con velocidad baja.
- **Medio**: 10 enemigos con velocidad media.
- **Difícil**: 12 enemigos con velocidad alta.

## Mecanismo del Juego
1. Al iniciar, el juego muestra un menú donde puedes seleccionar la dificultad.
2. La nave se puede mover de izquierda a derecha y disparar proyectiles.
3. Los enemigos se mueven horizontalmente y bajan cuando tocan los bordes.
4. Si un proyectil impacta a un enemigo, este reaparece en una posición aleatoria y se suma 1 punto al puntaje.
5. Cada 5 puntos, la velocidad de los enemigos aumenta.
6. Si un enemigo toca la nave, el juego finaliza automáticamente.




## Autor
Desarrollado por **Javier Andrés Sierra Pineda**.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
