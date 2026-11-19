
# Evaluación Unidad 3 - Programación Web

Aplicación web desarrollada con Python y Flask, que permite realizar dos ejercicios interactivos mediante formularios HTML.

## Tecnologías utilizadas

- Python
- Flask
- Jinja2
- HTML5
- CSS3

## Funcionalidades

### Ejercicio 1: Notas y asistencia

Permite ingresar tres notas y un porcentaje de asistencia para calcular el promedio y determinar si el estudiante aprueba o reprueba.

Para aprobar, se deben cumplir ambas condiciones:

- Obtener un promedio igual o superior a 40.
- Tener una asistencia igual o superior al 75%.

Además, se comprueba que los valores ingresados se encuentren dentro de los rangos establecidos.

### Ejercicio 2: Comparación de nombres

Permite ingresar tres nombres diferentes y comparar la cantidad de caracteres de cada uno.

El programa identifica el nombre con mayor cantidad de caracteres y contempla la posibilidad de que dos o incluso los tres nombres tengan la misma longitud.

Además, incorpora una comprobación para evitar que se ingresen nombres repetidos, incluso cuando se escriben utilizando distintas combinaciones de mayúsculas y minúsculas.

### Historial de actividades

La aplicación cuenta con una sección de historial donde se almacenan temporalmente los resultados de los ejercicios realizados.

Permite consultar los datos ingresados y eliminar registros individualmente.

Los registros se mantienen mientras la aplicación está en ejecución. Al reiniciarla, el historial vuelve a estar vacío.

## Idea de desarrollo

Después de crear las carpetas para organizar el proyecto, me pregunté a mí mismo si quería realizar un trabajo simple o intentar complicarme un poco más sin ninguna necesidad.

De esa pregunta surgió la idea de que quería que mi aplicación web tuviera una interfaz sencilla, pero también algo diferente que hiciera que el proyecto se sintiera un poco más personal.

Por esa razón, estuve considerando diferentes paletas de colores que representaran a algunos de mis Pokémon favoritos. Entre las opciones tenía a Gengar, Pikachu y Gardevoir. Sin embargo, después de realizar algunas pruebas de color, me di cuenta de que la que mejor quedaba era la paleta de Pikachu.

## Organización del proyecto

Después de desarrollar las páginas individuales, noté que varios elementos del código HTML se repetían. Por esa razón, decidí crear una plantilla base llamada `base.html`.

Esta contiene la estructura general de la aplicación, la cabecera, el pie de página y la conexión con el archivo CSS. Mediante los bloques de Jinja2, las demás páginas pueden reutilizar esta estructura y personalizar su contenido.

## Experiencia y aprendizaje

Desde antes de comenzar esta carrera, Python siempre me llamó la atención. Por esa razón, busqué durante mucho tiempo videotutoriales, cursos y diferentes formas de experimentar con este lenguaje de programación.

Sin embargo, algo a lo que jamás me había atrevido era intentar conectar Python con una página web. Por esa razón, no solo quise que esta evaluación cumpliera con lo que pedía el profesor, sino que también quería que se sintiera como un trabajo con sentido para mí.

No fue fácil realizar esta evaluación. Hubo momentos en los que no sabía qué hacer o dónde colocar cada cosa. También tuve que enfrentar algo que personalmente me cuesta mucho: dejar de pensar en cómo conseguir algo perfecto y buscar demasiadas alternativas para resolver un mismo problema, ya que de esa manera el proyecto parecía no terminar nunca.

Muchas veces se me dificultó entender HTML, especialmente porque tuve que aprenderlo al mismo tiempo que cursaba la asignatura y continuaba avanzando en la carrera.

También me detuve muchas veces a pensar en el usuario y en lo que vería la persona que tuviera acceso a este pequeño proyecto. Por eso, me debatí sobre si agregar o no algunos elementos adicionales, como el botón que permite regresar al menú principal o el efecto que aparece al pasar el cursor sobre los botones.

Sin embargo, como estos trabajos también están hechos para aprender, busqué información sobre esos temas e intenté incorporarlos a mi página web.

Finalmente, considero que esta evaluación fue una oportunidad para experimentar con herramientas que antes no había utilizado en conjunto y para aprender que un proyecto no necesita ser perfecto para tener valor.

## Instalación y ejecución

1. Clonar o descargar el repositorio.
2. Crear un entorno virtual.
3. Activar el entorno virtual en Windows.
4. Instalar las dependencias.
5. Ejecutar la aplicación.
6. Abrir el navegador.