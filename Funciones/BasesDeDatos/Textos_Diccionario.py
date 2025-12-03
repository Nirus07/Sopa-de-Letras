from Funciones.Rutas import Rutas

Textos = {
    "es":{
        "boton_Jugar": "Iniciar Juego",
        "boton_Ranking": "Ver Ranking",
        "boton_Ayuda": "Ayuda",
        "boton_Salir": "Salir",
        "boton_Ayuda": "Ayuda",
        "boton_Caracteristicas":"Características",
        "boton_Funcionalidades":'Funcionalidades',
        "boton_Reglas":"Reglas del Juego",

        # Botones Tipo de Juegos
        "Tradicional": "Tradicional",
        "Tradicional_Con_Tiempo": "Tradicional con Tiempo",
        "Contratiempo":"Contratiempo",
        "Versus":"Versus",

        # Botones Dificultades
        "Principiante": "Principiante",
        "Intermedia": "Intermedia",
        "Avanzada": "Avanzada",

        # Texto Palabras
        "Palabras":"Palabras",

        #  Texto Perdiste
        "Perdiste": "Se te acabo el tiempo, has perdido.",
        "Reintentar":"Reintentar",
        "Volver_al_Inicio":"Volver al Menú",

        # Texto Abandonar
        "boton_Abandonar": "Abandonar",
        "Abandonar": "¿Quieres abandonar el juego?",
        "Opcion_Si": "Si",
        "Opcion_No": "No",

        "Contra_Reloj_Estadisticas":"Contra Reloj",
        "Tradicional_Tiempo_Estadisticas": "Tradicional con Tiempo",
        "Versus_Estadisticas": "Versus",
        "Juegos_Generales": "Todos los Juegos",

        "boton_Mostrar_Solucion": "Mostrar Solución",
        "Jugador_A":"Jugador A",
        "Jugador_B":"Jugador B",

        # Sección Ranking / Estadísticas
        "Ranking_Tradicional_Tiempo": "Ranking Tradicional con Tiempo",
        "Ranking_Contratiempo": "Ranking Contratiempo",
        "Ranking_Versus": "Ranking Versus",
        "Ranking_General": "Historial de Juegos",
        "No_Hay_Registros": "No hay registros",

        # Seccion Ayuda
        "Caracteristicas": ("Caracteristicas: La sopa de letras cuenta con 4 tipos de juegos los cuáles son; Tradicional, Tradicional con tiempo, Contratiempo y Versus,"
        "estos tipos de juegos cuentan con sus dificultades las cuáles son; Principiante, Intermedio y Avanzado, dependiendo del tipo de juego"
        "se agregará un cronómetro ya sea Tradicional con tiempo o Versus y en el caso del temporizador es únicamente para el modo Contratiempo,"
        "este cronómetro o temporizador se visualizará en la parte izquierda,las dificultades generarán un sopa de letras más grande"
        "y con más palabras que se visualizarán en un cuadro al lado derecho, las palabras serán de forma aleatoria o bien las palabras "
        "seleccionadas por el jugador."
        ),
        "Funcionalidades": ("Funcionalidad: La sopa de letras cuentan con un sistema de asignación de palabras según la dificultad seleccionada, 6 palabras en principiante,"
        " 10 palabras en intermedio y 14 palabras en avanzada, estas palabras aparecen en el cuadro al lado derecho, el cuál al ser encontradas desaparecerá "
        "de la lista, también al marcar la palabra en la sopa se pintará de un color aleatorio para poder diferencia cada palabra encontrada, "
        "el juego cuenta con una opción para terminar el juego sin haber encontrado todas las palabras y se le mostrará un mensaje con la "
        "cantidad de palabras restantes, el juego cuenta con otra opción para mostrar la solución de la sopa de letras, mostrando cada palabra escondida en esta."
        ),
        "Reglas del Juego":("Reglas: \n1. El jugador debe seleccionar el modo y dificultad en la que quiera jugar.\n"
        "2. El jugador para poder estar en el ranking deberá completar algún tipo de juego.\n"
        "3. En el modo 'Versus' los jugadores en caso de no encontrar una palabra en un lapso de 2 minutos, perderá autómaticamente.\n"
        "4. El jugador puede seleccionar las palabras que desea encontrar en la sopa únicamente en la dificultad 'Principiante'.\n"
        ),

        # Rutas Imagenes

        "Inicio": Rutas.Inicio_es,
        "Selecciona_Juego":Rutas.Selecciona_Juego_es,
        "Dificultad": Rutas.Dificultad_es,
        "Ayuda": Rutas.Ayuda_es,
        "Consulta": Rutas.Consulta,
        "Ranking": Rutas.Ranking,

        "Regresar":"Regresar"
    },
    "en":{
        "boton_Jugar": "Start Game",
        "boton_Ranking": "Ranking",
        "boton_Ayuda": "Help",
        "boton_Salir": "Exit",
        "boton_Caracteristicas":"Characteristics",
        "boton_Funcionalidades":'Funcionality',
        "boton_Reglas":"Game rules",

        # Botones Tipo de Juegos
        "Tradicional": "Traditional",
        "Tradicional_Con_Tiempo": "Traditional with time",
        "Contratiempo":"Time Attack",
        "Versus":"Versus",

        # Botones Dificultades
        "Principiante": "Beginner",
        "Intermedia": "Intermediate",
        "Avanzada": "Advance",

        # Texto Palabras
        "Palabras":"Words",

        # Texto Perdiste
        "Perdiste":"Your time is up, you have lost.",
        "Reintentar":"Try Again",
        "Volver_al_Inicio":"Go to Menu",

        # Texto Abadonar
        "boton_Abandonar": "Quit",
        "Abandonar": "Do you want to quit the game?",
        "Opcion_Si": "Yes",
        "Opcion_No": "No",

        # Botones estadisticas
        "Contra_Reloj_Estadisticas":"Time Attack",
        "Tradicional_Tiempo_Estadisticas": "Traditional with Time",
        "Versus_Estadisticas": "Versus",
        "Juegos_Generales": "All Games",

        "boton_Mostrar_Solucion": "Show Solution",
        "Jugador_A":"Player A",
        "Jugador_B":"Player B",

        # Sección Ranking / Estadísticas
        "Ranking_Tradicional_Tiempo": "Traditional Time Ranking",
        "Ranking_Contratiempo": "Time Attack Ranking",
        "Ranking_Versus": "Versus Ranking",
        "Ranking_General": "Game History",
        "No_Hay_Registros": "No records found",

        # Help Section
        "Caracteristicas": (
            "Features: The word search game includes 4 game types: Traditional, "
            "Traditional with Time, Countertime, and Versus. These game types have "
            "different difficulty levels: Beginner, Intermediate, and Advanced. "
            "Depending on the game type, a timer will be added, either as a stopwatch "
            "in Traditional with Time or Versus, or as a countdown timer exclusively "
            "in the Countertime mode. This timer will be displayed on the left side. "
            "The difficulty levels generate a larger word search grid with more words, "
            "which will be shown in a panel on the right side. The words will be "
            "randomly selected or chosen by the player."
        ),

        "Funcionalidades": (
            "Functionality: The word search game uses a word assignment system based "
            "on the selected difficulty: 6 words in Beginner, 10 words in Intermediate, "
            "and 14 words in Advanced. These words appear in the panel on the right, "
            "and once found, they are removed from the list. When a word is selected "
            "in the grid, it will be highlighted with a random color to distinguish "
            "each found word. The game includes an option to end the game without "
            "finding all the words, showing a message with the number of remaining "
            "words. There is also an option to display the solution to the word search, "
            "revealing every hidden word in the grid."
        ),

        "Reglas del Juego": (
            "Rules:\n"
            "1. The player must select the game mode and difficulty they want to play.\n"
            "2. To appear in the ranking, the player must complete any game mode.\n"
            "3. The player can't select the words they want to search for only in "
            "any difficulty.\n"
        ),

        

        # Rutas Imagenes

        "Inicio": Rutas.Inicio_en,
        "Selecciona_Juego":Rutas.Selecciona_Juego_en,
        "Dificultad": Rutas.Dificultad_en,
        "Ayuda": Rutas.Ayuda_en,
        "Consulta": Rutas.Consulta,
        "Ranking": Rutas.Ranking,

        "Regresar": "Back"
    }
}