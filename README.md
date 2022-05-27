<div style="text-align: center">

# FiguRace

</div>

<div style="text-align: justify">

### Juego creado por Julia Caro, María Emilia Romero y Francisco Venegas Naboulet, para la asignatura "Seminario de Lenguajes - Opción Python"

#

Los directorios se encuentran orientados de la siguiente manera:

* `common`: Contiene las funciones comunes, que son transversales al proyecto
* `data`: Contiene los archivos generados para el procesamiento de datos dentro del juego
* `helpers`: Contiene los archivos con lógica particular para una o dos pantallas específicas
* `static`: Contiene aquellos archivos que son estáticos al proyecto
* `windows`: Contiene los archivos en los que se dividen las pantallas del juego
* `figurace.py`: Es el archivo main del proyecto

#

</div>

<div style="text-align: center">

## ¿Cómo jugar?

</div>

<div style="text-align: justify">

**FiguRace** es un juego educativo basado en tarjetas. Para ello, se muestra en pantalla una serie de datos al usuario, con características de la tarjeta que permitirán que el usuario identifique la misma. Por ello, el jugador deberá adivinar a qué hace referencia la tarjeta, dentro de un tiempo configurable. 

Al ejecutar el juego, se mostrarán la pantalla inicial del menú, con las opciones:  
`Jugar` - `Perfil` - `Puntajes` - `Configuración`

</div>

<div style="text-align: center">

### Jugar

</div>

<div style="text-align: justify">

Cuando se elige esta opción, inicia el juego. La pantalla mostrará, por un lado, la dificultad y nickname elegidos por el usuario. 
Por el otro, presentará la tarjeta con carácterísticas de lo que el usuario debe adivinar, con opciones para que pueda marcar según cual crea que sea la correcta. Esto puede ser un lago, una película o una canción de acuerdo a lo que el mismo elija.
Adicionalmente, contará con botones que permitan avanzar, pasar o abandonar el juego de acuerdo a lo que desee el usuario.  

</div>

<div style="text-align: center">

### Perfil

</div>

<div style="text-align: justify">
La selección de esta ventana permitirá al usuario crear y/o editar perfiles. En la misma, en caso de `crear un nuevo perfil`, se deberá indicar Nick (Apodo), Edad, Género autopercibido y Contraseña de la persona que jugará. Adicionalmente, si se selecciona la opción de `edición de perfil`, se deberá indicar el Nick del usuario a modificar y el usuario deberá ingresar los nuevos datos.  

</div>

<div style="text-align: center">

### Puntajes

</div>

<div style="text-align: justify">

Esta pantalla mostrará los datos de los 20 mejores puntajes, por cada nivel, junto con el Nick del jugador que lo obtuvo.

</div>

<div style="text-align: center">

### Configuración

</div>

<div style="text-align: justify">

El programa permitirá seleccionar la dificultad del juego, entre `Fácil`, `Media` y `Dificil`. Adicionalmente, se listarán una serie de parámetros en las que el usuario podrá modificar a su gusto vinculados con la jugabilidad, como el tiempo límite por ronda, cantidad de rondas, cantidad de características a mostrar, entre otros.
Por último, una vez elegida la dificultad y establecidos los parámetros, el usuario, a su vez, podrá seleccionar el set de datos con el que quiera jugar.

</div>

#