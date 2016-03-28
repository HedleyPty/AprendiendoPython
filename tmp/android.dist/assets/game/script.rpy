init python:
    persistent.console=False
    subtitle = Position(xpos=0.5, xanchor='center', ypos=0.60,
                   yanchor='top')
    def cambiarMusica(m):
        global musica, now_playing
        lm=['The Show Must Be Go.mp3','Poofy Reel.mp3']
        lm.remove(m)
        musica = lm[0]
        now_playing=musica[:-4]
        renpy.play(musica, 'music')
    
    
image python_logo =Image("images/Python logo.png",xalign=0.5, yalign=0.5)
image renpy_logo =Image("images/renpy logo.png", xalign=0.5, yalign=0.2)
image reloj=im.FactorScale("images/reloj.png", 0.25)
image reloj guts=im.FactorScale("images/reloj engranajes.jpg", 0.25)
image white ="#ffffff"
define h = Character('Hedley', color="#c8ffc8")
define consola = Character('Consola de Python', color="#00cc00")
$tipJar="https://www.paypal.me/HedleyQuintana"

# The game starts here.
# - El juego comienza aquí.

label start:
    $ musica = ""
    $ current="inicio"
label music_:
    scene white with dissolve
    if musica:
        play music musica
        menu:
            "¿La dejas tocando?"
            "Sí":
                $renpy.jump(current)
            "No, quiero cambiarla":
                stop music
            "No, prefiero estar en silencio":
                stop music
                jump inicio
    menu mus:
        "Seleccione la melodía de fondo, "
        "Poofy Reel":
            $ musica = "Poofy Reel.mp3"
            $renpy.music.set_volume(0.3, delay=0, channel='music')
            jump music_
        "The Show Must Be Go":
            $ musica ="The Show Must Be Go.mp3"
            $ renpy.music.set_volume(0.3, delay=0, channel='music')
            jump music_
        "Ninguno":
            pass
label inicio:
    $ now_playing=musica[:-4]
    #textbutton "Music" action Show("_music") 
    show python_logo at truecenter
    show text "{color=#000000}Logo de Python{/color}" at subtitle
    show screen _music
    h "Saludos a todos, me llamo Hedley!"
    h "Soy un médico gradudado de la Universidad de Panamá, tengo una maestría en Biología molecular y estoy estudiando un doctorado en epidemiología en el Instituto Karolinska"
    h "No se si sea el más adecuado, pero les voy a enseñar lo poco que sé de Python"
    h "Y para sonar más interesante, les digo..."
    show renpy_logo:
        xpos 0.8
        ypos 0.2
    show text "{color=#000000}Logo de Ren'py{/color}" at Position(xpos=0.80, xanchor='center', ypos=0.65, yanchor='top')
    h "que este tutorial, está desarrollado en Ren'py el cual es una implentación de Python"
    h "Ren'py es un gestor de {color=#ff0}novelas gráficas interactivas{/color}, las cuales son una serie de {color=#ff0}diálogos{/color} (así como una telenovela, pero leída).\nAparecen dibujos de personajes que aparecen con su cuadro de diálogos"
    h "Además hay menúes que sirven para valorar el conocimiento de la trama o para tomar decisiones"
    h "Más adelante tendremos acceso a una herramienta de Ren'py que nos va a ayudar a comprender mucho mejor los conceptos aquiridos en este tutorial"
    hide renpy_logo 
    hide text
    h "Vamos a empezar..."
    #hide text
    jump chp1
label chp1:
    show text "{size=40}{color=#000}Capítulo uno\n\n\n¿Qué es programar?{/color}{/size}" at top
    h "Para mi, aprender a programar me pareció bastante frustrante!"
    h "Verán, aprendí varios lenguajes de programación, pero no supe lo que era programar..."
    h "Vamos a intentar aprender a programar antes de entrar de lleno a Python"
    h "Vamos a iniciar con el concepto del {color=#ff0}proyecto{/color}"
    h "Los {color=#ff0}proyectos{/color} están asociados a 2 conceptos:"
    h 'El primero es que el proyecto debe tener la finalidad de {color=#ff0}resolver un problema{/color}'
    h 'El {color=#ff0}problema{/color} es de caracter repetitivo y se resuelve mediante la {color=#ff0}interacción{/color} de partes de un {color=#ff0}sistema{/color}'
    h "El {color=#ff0}sistema{/color} es el segundo concepto"
    h "Las partes del sistema están contenidas en una {color=ff0}carpeta{/color} o un {color=#ff0}directorio{/color} dentro de la {color=#ff0}computadora{/color} (llamado en España{color=#ff0}\"ordernador\"{/color}) o en la {color=#ff0}nube{/color}"
    $current="q1"
    $ error=""
    label q1:
        if error != "":
            h "{color=#f00}[error]{/color}"
        hide python_logo
        menu:
            "¿Cuál de los siguientes conceptos NO están asociados al concepto del proyecto"
            "La nube":
                jump q2
                
            "Resolver un problema con un fin específico":
                $error="en efecto, eso es correcto, busca la opción {color=#ff0}incorrecta{/color}"
                $renpy.jump(current)
                
            "Una carpeta con piezas de un sistema":
                $error="Las carpetas usualmente se asocian a un proyecto: eso es correcto, busca la opción {color=#ff0}incorrecta{/color}"
                $renpy.jump(current)
            "Un sistema con partes que interaccionan entre ellas":
                $error="Esto es correcto, un {color=#ff0}sistema{/color} tiene partes que interaccionan entre ellas"
                $renpy.jump(current)
    label q2:
        show python_logo at truecenter
        h "La nube es la opción incorrecta! vamos adelante"
        h "Vamos a ver un ejemplo tangible"
        h "Veamos un reloj..."
        hide python_logo
        show reloj at truecenter
        h "El reloj analógico es un {color=#ff0}sistema complejo{/color} que permite saber la hora"
        h "Mediante el movimiento de sus 3 manecillas a diferentes velocidades"
        hide reloj
        show reloj guts at truecenter
        h "para serles sinceros no se como trabajan los relojes, pero lo que sí se"
        h "es que los engranajes (o ruedas dentadas) trabajan de manera coordinada a {color=ff0}diferentes velocidades{/color} para posicionarse"
        h "y contestar a la pregunta {color=#ff0}\"¿Qué hora es?\"{/color}"
        h "Las manecillas se mueven de forma implacable con el pasar de tiempo..."
        h "Vamos a repasar lo aprendido acerca de los relojes en relación a la programación"
        $ error=""
        hide reloj guts
        jump q3
    label q3:
        
        if error !="":
            h "{color=#f00}[error]{/color}"
        menu:
            "¿Cuál de las siguientes afirmaciones es correcta?"
            "El reloj es un sistema simple para resolver una pregunta compleja":
                $error= "¿No es al revés?"
                jump q3
            "Las manecillas del reloj se mueven a la misma velocidad":
                $error = "Así no funcionan los relojes"
                jump q3
            "Los relojes son máquinas complejas que poseen partes sencillas":
                $error= ""
                jump partes1
    label partes1:
        show python_logo at truecenter
        h "¡En efecto! aunque el reloj es una máquina aparentemente compleja, que tiene partes sencillas"
        h "Regresando a los proyectos, los proyectos tienen una serie de partes que se relacionan entre sí..."
        h "Pero para serles sinceros no soy un relojero, y conozco muy poco acerca de como funcionan esos aparatos"
        h "Sin embargo, podemos {color=#ff0}imaginar{/color} o deducir de manera correcta que el reloj analógico está compuesto de {color=#ff0}piezas{/color} que trabajan de manera {color=#ff0}coordinada{/color}"
        h "Teniendo en cuenta esto..."
        hide python_logo
        $ count=0
        $error =""
        jump q4
label q4:
    if error:
        h "{color=#f00}[error]{/color}"
    menu:
        "¿Cuál de estos sistemas complejos, no tiene piezas más simples?"
        "Un carro":
            $ error="No tienes idea lo que cuesta cambiar las {color=ff0}piezas{/color} cuando se daña o lo chocan"
            $ count += 1 
            jump q4
        "El cuerpo humano":
            $error=" Creo que le has quitado el pan a un cirujano...."
            $count += 1
            jump q4
        "Una página web":
            $error="Las páginas web son sistemas muy complejos que interaccionan con el usuarios, tienen una serie de piezas más simples otras páginas, manejan bases de datos, en fin todo un enredo"
            $count += 1
            jump q4
        "Un juego de vídeo":
            $error="Los juegos de video son sistemas muy complejos que interaccionan con el usuarios: tienen piezas más simples que manejan a enemigos, al puntaje, en fin todo un enredo"
            jump q4
        "Clavos":
            h "Eso es correcto!!!"
            jump n2
label n2:
    show python_logo at truecenter
    if error == "":
        h "Veo que has acertado a la primera..."
        h "Sin embargo, más adelante verás que cometer errores es muy importante para programar"
    else:
        h "Has seleccionado [count] veces la opción incorrecta"
        h "Cometer errores, es muy importante para aprender cualquier lenguaje de programación..."
    show python_logo at truecenter
    h "Existen 2 grandes fases en la programación, la etapa de {color=#ff0}desarrollo{/color} y la etapa de {color=#ff0}producción{/color}"
    h "En la etapa de desarrollo, se DEBEN cometer errores para evitar que éstos vayan a producción"
    h "Además debemos saber que existen 2 tipos de errores: los errores de {color=#ff0}sintaxis{/color} y los errores de {color=#ff0}lógica{/color}"
    h "Los errores de {color=#ff0}sintaxis{/color} impiden al programa traducirse desde el lenguaje de programación el programa NO CORRE"
    h "Es decir que el programa no corre durante el {color=#ff0}tiempo de ejecución{/color} conocido en inglés como {color=#ff0}runtime{/color}"
    h "Los errores de lógica permiten al programa correr, pero el resultado NO es el esperado"
    h "Un ejemplo de un error de lógica sería un programa que imite a un reloj analógo, el cual CORRE, pero todas las manecillas se mueven a la misma velocidad"
    h "Los errores lógicos son definitivamente muy difíciles de detectar y pueden pasar a la etapa de {color=#ff0}producción{/color} si no somos cuidadosos"
    h "Regresando a la pregunta anterior"
    h "Veo que han notado que a diferencia de objetos o sistemas, los {color=#ff0}clavos{/color} son objectos bastante {color=#ff0}simples{/color}."
    h "Ellos no tienen otras partes dentro y pueden servir para crear objetos más grandes y complejos"
    
    h "El ejercicio de imaginarse como podemos \"desmembrar\" un sistema complejo en sus componentes fundamentales y sus relaciones es el primer paso para poder programar"
    h "A esto se le llama {color=#ff0}abstracción{/color}"
    h "En Python, tenemos algo equivalente a los clavos, pedazos de madera, tornillos o unidades fundamentales"
    h "Los cuales nos van a ayudar a construir sistemas muy complejos"
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    h "La abstracción es tratar de sacar cada una de las piezas que forman un sistema"
    h "Y elaborar un programa con sus partes y las interacción entre esas piezas"
    h "Veamos un ejemplo"
    $count=0
    $error=""
    hide text
    hide python_logo
    jump q5
label q5:
    if error != "":
        h "{color=f00}[error]{/}"
    menu:
        "Uno de los siguientes no forman parte del sistema digestivo"
        "El estómago":
            $ error= "estás bromeando?"
            jump q5
        "La tráquea":
            $del error
            jump n3
        "El hígado":
            $error = "El hígado pertenece al aparato digestivo, pero no es parte del \"tubo digestivo\".\nCreo que hay una mejor opción"
            jump q5

label n3:
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    show python_logo at truecenter
    h "Qué pregunta más tonta..."
    h "Es cierto que a la tráquea le llega comida de cuando en cuando..."
    h "Pero no en personas sanas..."
    h "Ya que hablamos del sistema digestivo... vamos a hacer algo en relación al mismo"
    python:
        digestivo=["boca","faringe","esófago", "estómago", "intestino delgado", "intestino grueso", "ano"]
        check_organ=""
        counter=9
        
    hide text
    hide python_logo
    jump q6
label q6:
    if counter == 9:
        python:
            cabecera= "Señale el órgano del tubo digestivo que se encuentra en la cabeza"
            counter = 0
    else:
        if counter < 6:
            if check_organ == digestivo[counter]:
                python:
                    counter += 1
                    organo = check_organ
                if counter < 3:
                    $cabecera = "Qué órgano sigue a la "+ organo
                else:
                    $cabecera="Qué órgano sigue al " + organo
            else:
                if counter > 0 and counter < 5 :
                    h "{color=#f00}Ese órgano no es el que sigue!{/color}"
                else:
                    h "{color=#f00}Ese órgano no está en la cabeza!{/color}"
            
    
        elif counter == 6:
            h "Y así tenemos que el último órgano del sistema digestivo es el ano"
            jump n4
    menu:
        "[cabecera]"
        
        "Ano":
            $check_organ=digestivo[6]
            jump q6
        "Faringe":
            $check_organ=digestivo[1]
            jump q6
        "Esófago":
            $check_organ=digestivo[2]
            jump q6
        "Boca":
            $check_organ=digestivo[0]
            jump q6
        "Intestino delgado":
            $check_organ=digestivo[4]
            jump q6
        "Estómago":
            $check_organ=digestivo[3]
            jump q6
        "Intestino grueso":
            $check_organ=digestivo[5]
            jump q6
label n4:
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    h "Wao, hemos visto como se conectan los órganos del tubo digestivo uno tras otro"
    h "En el caso del carro, del reloj, la página web y del video juego podemos hacer exactamente lo mismo..."
    h "Aún más NO necesitamos ningún programa para ver como estos elementos se relacionan entre sí"
    h "Podemos agarrar un pedazo papel y describir los elementos, su comportamiento, como se relacionan unos con los otros "
    h "Este {color=#ff0}diseño{/color} es fundamental para saber las acciones y definir nuestro programa"
    h "Creo que estamos listos para ver como representamos esos sistemas y elementos en nuestro programa"
    h "Antes de hablar de como hacer esas {color=#ff0}abstracciones{/color} en Python tengo que mostrarles el equivalente a los clavos, engranes y otras piezas fundamentales para crear sistemas complejos"
    h "En Python (como cualquier otro idioma de programación) estos son: las {color=#ff0}variables{/color}, los {color=#ff0}operadores{/color} y las {color=#ff0}funciones{/color}"
    hide text
label python_:
    show text "{size=40}{color=#000}Capítulo tres\n\n\nPython, la línea de comandos y los scripts (libretos){/color}{/size}" at top
    h "Pero antes de proseguir, debo interrumpar para hablar acerca de como Python trabaja"
    h "El primer lugar donde vamos a trabajar es en la {color=#ff0}línea de comandos{/color} o {color=#ff0}consola Python{/color}"
    h "La consola ejecuta una {color=#ff0}sentencia{/color} en inglés llamada {color=#ff0}statement{/color}"
    h "En la consola se corre una línea a la vez y el resultado se observa al presionar {color=#ff0}enter{/color} llamado en español castizo {color=#ff0}salto de carro{/color}"
   
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLas variables{/color}{/size}" at top
    h "Antes de examinar el concepto de las variables en Python, vamos a instalarlo"
    h "Python es un idioma multiplataforma"
    h "Es decir como casi todos los lenguajes de programación, este crea programas el cual va a correr independientemente del sistema operativo despues de traducirse al {color=#ff0}un programa específico de ese sistema operativo{/color}"
    h "Esta traducción se llama {color=ff0}compilación{/color}"
    h "Si estás corriendo este tutorial desde una computadora u ordernador que corre Mac OS o Windows, debes ir a la página web de Python donde puedes bajar el instalador para la plataforma en la página de {a=https://www.python.org/downloads/}descargas de Python{/a}"
    h "Si lo corres en Linux, debes usar el instalador de paquetes de instalación correspondiente (preferiblemente) o compilar los binarios de la página web oficial: {a=https://www.python.org/downloads/source}Compiladores de Python{/a}"
    h "Si estás corriendo esto en Android hay 2 maneras de correr Python"
    h "la forma \"difícil\" que es instalando una aplicación de terminal e instalando Python desde allí (por cierto este método ocupa mucho espacio en el celular)"
    h "O bajando el app \"QPython\", el cual le va a dar los elementos necesarios para correr python en su teléfono inteligente o tableta"
    
    $ persistent.console=True
    
    h "Una vez que hayas hecho eso, podemos seguir..."
    h "Las variables son un objecto que contiene cierta información que se va a reutilizar más tarde"
    h "En alguno de los ejercicios anteriores, he usado variables, por ejemplo... te acuerdas cuando conté el número de errores los ejercicios anteriores? esa información la guardé en una variable"
    h "Para crear una variable, debemos tener 3 elementos: el {color=#f00}nombre de la variable{/color}, el {color=#f00}operador de asignación{/color} y su {color=#f00}valor{/color}."
    h "Un ejemplo a = 16.29\na es el nombre de la variable\n= es el operador de asignación\n16.29 es el valor de la variable"
    h "Es importante destacar que hay ciertas reglas para nombrUar una variable"
    h "Las variables puedes nombrarla \"como quieras\" (lo pongo entre comillas por algo), pero su nombre solo puede contener signos de subrayado(_), letras (sin carácteres especiales, tildes o la ñ) y números."
    h "Por supuesto, no menciono signos de puntuación ni espacios, porque no están permitidos"
    h "Las variables tampoco pueden ser \"palabras reservadas\" del lenguaje Python, las cual aprenderemos más adelante, dichas palabras son de uso común en inglés, pero no en español"
    h "Y el nombre nunca puede iniciar con un número"
    h "Para reutilizar la variable debemos escribir respetando las mayúsculas y minúsculas: la variable A no es lo mismo que la variable a"
    h "Ok, vamos a repasar lo aprendido"
    $ error=""
    hide text
label q7:
    if error!="":
        h "Epa! El nombre [error] es perfectamente legal"
    if error=="_import":
        h "import es un nombre ILEGAL en Python y no lo puedes usar"
        h "Más adelante verás por qué..."
        h "Sin embargo, tanto _import como import_ son nombres permitidos"
    menu:
        "Cual de los siguientes nombres {color=#ff0}no{/color} es permitido en Python"
        "_asTAS45":
            $ error= "_asTAS45"
            jump q7
        "2_Temporada":
            $ error =""
            h "CORRECTO"
            jump n5
        "Asteroide4":
            $ error="Asteroide4"
            jump q7
        "_import":
            $ error = "_import"
            jump q7
label n5:
    show text "{size=40}{color=#000}Capítulo tres\n\n\nLas variables{/color}{/size}" at top
    h "En verdad, es correcto, las variables no pueden iniciar su nombre con números"
    h "De todos los casos presentados anteriormente, quiero que presten atención a \"_asTAS45\""
    h "Como deben saber a estas alturas, \"_asTAS45\" es un nombre Python permitido, porque cumple con las reglas del lenguaje, pero..." 
    hide text

label q8:
    if error != "" :
        h "{color=#f00}[error]{/color}"
    menu:
        'Que problema presenta la variable "_asTAS45", a diferencia de "Asteroide4" y la variable "_import"'
        ""
        "No veo ningun problema con ese nombre":
            $error ='Ponga atención a las otras opciones\nCompárelo con las otros 2 variables y dígame que tiene de "raro" ese nombre'
            jump q8
        "No es posible saber que se trata fácilmente":
            $error=""
            h "EXACTO"
            jump n6
        "Python va a detectar un error incluso si tiene un nombre legal":
            $error ="Python no ve nada raro en la variable, usted como humano puede ver algo que Python no ve"
            jump q8
label n6:
    show text "{size=40}{color=#000}Capítulo tres\n\n\nLas variables{/color}{/size}" at top
    h 'En verdad... "_asTAS45" es un nombre que no significa nada, bueno de buenas a primeras'
    h "Las variables Astoide4 y la variable _import tienen algun sentido:\nAsteriode4 puede significar algun asteroide en un juego de video o algo relacionado con astronomía\n_import puede significar que se a importar algo..."
    h "La idea de Python es de servir como un lenguaje de \"alto nivel\", es decir ser \"entendible\" para los humanos"
    h "Aunque no tanto para el ordenador o computadora"
    h "Variables con un nombre como \"_asTAS45\" hacen que todo se enrede a menos que tenga una lógica interna"
    hide text
label q9:
    menu:
        "Python es un lenguaje de programación de alto nivel, ¿qué significa esto?"
        "Que Python es mucho más comprensible para los humanos que leen el programa que para las máquinas donde se corre":
            h "CORRECTO"
            jump n7
        "Que Python es mucho más comprensible para las máquinas donde se corre que para los humanos que leen el mismo":
            h "¡Eso no es correcto!"
            jump q9
        "Que es un lenguaje de alto nivel de complejidad":
            h "Ciertamente se pueden crear programas muy complejos con Python"
            h "Pero eso no tiene nada que ver con el nivel de lenguaje"
            h "¡Eso no es correcto!"
            jump q9
label n7:
    show text "{size=40}{color=#000}Capítulo tres\n\n\nLas variables{/color}{/size}" at top
    h "El mensaje es que las variables deben comunica la \"finalidad\" dentro del proyecto"
    h "Vamos a crear otra variable..."
    python:
        varnam=""
        asignacion=""
        valor=""
        error=""
    hide text
label q10:
    $cont="Cree la variable segun las instrucciones"
    if error:
        h "Opa! Python nos muestra un error"
        h "{color=#ff0}[error]{/color}"
        $error=""
    $encabezado="Vamos a crear una variable peso_varon la cual representa el peso de un varón de 70 kg, señale las partes de la variable"
    if varnam or asignacion or valor:
        $encabezado += "\n>>>" + varnam +" " + asignacion + " " + valor
        if varnam and asignacion and valor:
            $cont="Presione aquí para continuar"
    menu:
        consola "[encabezado]"
        "peso_Varon":
            $varnam="peso_Varon"
            jump q10
        "peso Varon":
            $error='  File "<stdin>", line 1\n    peso Varon\n             ^\nSyntaxError: invalid syntax'
            jump q10
        "=":
            $asignacion="="
            jump q10
        "70 kg":
            $error='  File "<stdin>", line 1\n    ...70 kg\n         ...^\nSyntaxError: invalid syntax'
            jump q10
        "70":
            $valor="70"
            jump q10
        "[cont]":
            if varnam and asignacion and valor:
                jump n8
            else:
                jump q10
label n8:
    show text "{size=40}{color=#000}Capítulo tres\n\n\nLas variables{/color}{/size}" at top
    h "Como vemos las variables pueden ser creadas escribiendo su nombre su nombre, luego el operador de asignación (=) y finalmente el valor"
    h "Además del signo =, hay otros signos de asignación que veremos más adelante"
    h "En el siguiente ejercicio te voy a mostrar ejemplo de otros operadores, pero para poder entenderlos, debo hablarte de los {color=#ff0}tipos{/color} de variables"
    h 'Existen varios tipos de valores, en la variable peso_Varon le asignamos un valor de 70 que es {color=#ff0}número entero{/color} o un en lenguaje Python un {color=#ff0}int{/color}'
    h 'Las variables además pueden ser de tipo número "flotante" ("float" en ingles e idioma Python), "cadena" ("string" en inglés y str en idioma Python), booleana ("bool" en idioma Python)'
    h "Python deduce el tipo de variable como número entero ({color=#ff0}int{/color}), si escribimos un número sin el punto decimal:\n{color=f0f}#Por ejemplo{/color}\npeso_Varon=70 es de tipo int"
    h "Nota que escribi en nuestra consola {color=f0f}#Por ejemplo{/color} y que no hubo mensaje de error."
    h "Esto se debe a que este es un {color=#f0f}comentario{/color}, los cuales NO SE CORREN"
    h "Ellos sirven para indicarnos que de que se trata la variable, la función o el código que está debajo"
    h "¿Recuerdas que habíamos hablado de como las partes se relacionan entre ellas? y como cada parte del proyecto se relaciona una con la otra"
    h "Los comentarios pueden ayudarnos a escribir un código de manera eficiente escribiendo en buen español las relaciones que habíamos hecho en el papel..."
    h "Después de esta pequeña interrupción continuamos hablando de los otros tipos de las variables"
    h "Para saber el tipo de una variable, solo debemos escribir {color=#ff0}type{/color} seguido por el nombre de la variable:\ntype(peso_Varon)\n\<type 'int'\>"
    h "Python deduce el tipo de variable como número flotante ({color=#ff0}float{/color}), si escribimos un número con el punto decimal\n"
    consola "{color=#f0f}#Por ejemplo{/color}\n{color=#ff0}peso_Mujer=70.0\ntype(peso_Mujer)\n\<type 'float'\>{/color}"
    consola "{color=#f0f}#O también, puedes omitir los ceros{/color}\n{color=#ff0}peso_Mujer=70. {color=#f0f}#Nota que no hay ceros{/color}\ntype(peso_Mujer)\n\<type 'float'\>{/color}"
    h "Python deduce el tipo de variable como cadena ({color=#ff0}str{/color}), si escribimos cualquier cosa entre un par de comillas dobles \"\" o simples ''"
    consola "{color=#f0f}#Por ejemplo{/color}\n{color=#ff0}peso_infante='20.0 kilogramos'\ntype(peso_infante)\n\<type 'str'\>{/color}"
    h "Y finalmente las variables booleanas, son la que solo pueden tener 2 valores cierto o {color=#ff0}True{/color} y falso {color=#ff0}False{/color}"
    h "Vamos al siguiente ejercicio"
    hide text
    $counter=0
    $check=""
label q11:
    $tipos=["str", "float", "int", "float","bool"]
    $valores=['"Rosa"', "60.5", "123", "24.", "False"]
    
    if check=="":
        pass
    elif check == tipos[counter]:
        h "CORRECTO"
        $counter += 1
        if counter == 5:
            h "Has determinado los tipos de las variables, vamos a proseguir hablando de los operadores aritméticos y lógicos"
            jump n9
    else:
        h "¡Eso no es correcto!"
    $encabezado="#Determine el tipo Python de la variable cuyo valor es: " + valores[counter]
    menu:
        consola "[encabezado]"
        "int":
            $check="int"
            jump q11
        "str":
            $check="str"
            jump q11
        "float":
            $check="float"
            jump q11
        "bool":
            $check="bool"
            jump q11
label n9:
    h "Ya sabemos como crear variables... ahora vamos a hablar que hacer con ellas, vamos a aprender acerca de los operadores"
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "Los operadores nos permiten crear nuevas variables o resultados a partir de 2 o más variables o valores"
    h "Los primeros operadores que vamos a ver son los {color=#ff0}operadores aritméticos{/color}, los cuales crean nuevos números a partir de otros números"
    h "Los operadores aritméticos que vamos a ver son el de la suma {color=#ff0}+{/color}, la resta {color=#ff0}-{/color}, la multiplicación {color=#ff0}*{/color}, la división {color=#ff0}/{/color}, el residuo {color=#ff0}\%{/color} y la exponenciación {color=#ff0}**{/color}"
    h "La suma y la resta son bastante sencillas, veamos unos ejemplos"
    consola "1+1\n2"
    consola "3-2\n1"
    consola "24-45\n-21"
    h "Claro está... debemos recordar que hay dos tipos de varibles numéricas, las de tipo entera ({color=#ff0}int{/color}) y las de tipo flotante que manejan decimales ({color=#ff0}float{/color})"
    h "La suma o resta de dos o más variables de tipo entera producen un entero, y si hay por lo menos una variablo de tipo flotante, se produce un resultado flotante"
    consola "{color=#ff0}#Es decir{/color}\n1+1\n2\n1.2+1\n2.2\n2.3-1-3\n1.7"
    h "Tengo buena memoria y me acuerdo que creamos un par de variables peso_Varon y peso_Mujer"
    $error=""
    hide text
label q12:
    if error:
        h "[error]"
    menu:
        "Recordemos que peso_Varon tiene un valor de 70 y peso_Mujer de 70.0\n¿Cuál es el valor de peso_Varon-peso_Mujer ?"
        "0":
            $error="Eso no es correcto"
            jump q12
        "0.0":
            h "CORRECTO" 
            h "La suma de un entero y un número flotante da como resultado un flotante"
            jump n10
        "False":
            $error="Eso no es correcto\nEsa es una variable boolean, los operadores aritmeticos nunca resultan en una variable boolean"
            jump q12
        "None":
            $error="Eso no es correcto\nEsa es una variable tipo None, los operadores aritmeticos nunca resultan en ese tipo de variable"
            jump q12
label n10:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "La multiplicacion, la división y el residuo son un poquito especiales"
    h "Igual que lo que ocurre con la suma y la resta, estás operaciones entre enteros resultan en un entero y si hay por lo menos un flotante involucrado, tendremos un flotante"
    h "En el caso de la multiplicación, eso no es mucho problema"
    consola "{color=#f0f}#Multiplicacion de enteros{/color}\n3*5\n15"
    consola "{color=#f0f}#Multiplicacion con flotantes{/color}\n3.0*5.*8.0\n90.0"
    consola "{color=#f0f}#Multiplicacion con por lo menos un enteros{/color}\n3.0*5*8\n90.0"
    h "En el caso de la división es un poco especial, debido que al dividir, no vamos a obtener necesariamente un número entero"
    h "Si dividimos dos enteros vamos a obtener la {color=#ff0}parte entera de la division{/color}"
    consola "{color=#f0f}#Sabemos que 48 entre 8 es 6{/color}\n48/8\n6"
    consola "{color=#f0f}#Pero 50 entre 8 tambien es 6{/color}\n50/8\n6"
    consola "{color=#f0f}#Aun más 55 entre 8 tambien es 6{/color}\n55/8\n6"
    consola "{color=#f0f}#Claro está 56 entre 8 es 7{/color}\n56/8\n7"
    h "Las operaciones con flotantes, se toman en cuenta los decimales por lo que.."
    consola "{color=#f0f}Aun más 55 entre 8 es 6.87{/color}\n55.0/8\n6.87"
    h 'El residuo es lo "sobra" despues de dividir con enteros'
    h 'Es decir, 55 entre 8 es 6, pero como 6*8 es 48, el "residuo" sería 7 es decir 55-48 es 7'
    consola "55\%8\n7"
    consola "23\%5\n3"
    h "El residuo es importante para valorar los números pares de los impares"
    h "Los números pares al dividirse entre 2 tienen un residuo de 0, pero los impares tienen un residuo de 1"
    hide text
    $error=""
label q13:
        if error:
            h "[error]"
        menu:
            consola "#¿Cuanto es el valor de 135\%2?"
            "0":
                $error="Eso no es correcto"
                jump q13
            "1":
                h "¡Exacto! seguimos adelante!"
            "2":
                $error="Eso no es correcto"
                jump q13
            "135":
                $error="Eso no es correcto"
                jump q13
label n11:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "Bueno... voy a discutir acerca de la exponenciación, la cual es parte de parte de la aritmética...."
    h "En la exponenciación hay dos elementos, la base y el exponente"
    #text ...
    h "En la exponenciación, la base debe multiplicarse por si misma las veces indicadas por el exponente"
    h "En Python, la exponenciación se realiza asi: base**exponente"
    h "5*5 es 25 y 9*9*9 es 729\n,tambien 5**2 es 25 y 9**3 es 729"
    h 'En matemáticas (mas no en Python), el exponente 2 se le llama "cuadrado" y al exponente 3 se llama "cubo", los que siguen mediante números cardinales: 4 "elevado a la cuarta", 5 "elevado a la quinta", etc'
    h "El exponente 0 siempre da como resultado 1, y el exponente 1 da como resultado la base"
    h "#Es decir que el exponente 0 da como resultado 1\n454655**0\n1"
    h "#Y el exponente 1 da como resultado la base\n454655**1\n454655"
    h "Seguimos hablando de la exponenciación... "
    h "Sabemos que la resta es lo opuesto a la suma y la división es lo opuesto a la multiplicación"
    consola "{color=#f0f}#En el caso de la suma:{/color}\n2+3\n5\n#Y su operación opuesta es la resta\n5-3\n2"
    consola "{color=#f0f}#En el caso de la multiplicación:{/color}\n5*6\n30\n#Y su operación opuesta es la división\n30/5\n6"
    h "En la exponenciación tenemos 2 operaciones opuestas: la \"radicación\" y el \"logaritmo\""
    #Figura de la radicación
    h "En el caso de la radicación tenemos 2 componentes, que son el radical y el índice"
    h "El objetivo de la radicación es obtener el número que al multiplicarse por si mismo las veces dadas por el índice da por resultado el radical"
    h "Los índides siguen las mismos nombres (en matemáticas) de los exponentes de la exponenciación: raíz cuadrada (2), raíz cúbica (3), raíz cuarta (4), etc "
    h "Por ejemplo, la raíz cuarta de 1296 es 6, porque 6*6*6*6 es 1296 o bien 6**4 es 1296"
    hide text
label q14:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "**Python no tiene ninguna función (de manera predefinida) para calcular raíces"
    h "Sin embargo, es posible calcular cualquier raíz de cualquier índice usando uno de los 2 métodos"
    h "Un método es primero importar un módulo llamado math y luego usar un método llamado sqrt"
    h "Si usamos este método SOLAMENTE podemos calcular raíces con indices pares..."
    h "Vamos a calcular la raíz cuadrada de 25 (que sabemos que es cinco)"
    h "Lo primero es importar el módulo de mas matemáticas"
    h "Lo hacemos con la palabra reservada {color=#ff0}import{/import}"
    consola "{color=#f0f}#Es decir{/color}\nimport math"
    h "Y luego usamos el metodo sqrt de math asi"
    h "{color=#f0f}#Raiz cuadrada de 25{/color}\nimport math\nmath.sqrt(25)\n5.0"
    h "También podemos dar un alias más amigable al módulo usando la palabra reservada {color=#ff0}as{/color} que en inglés significa {color=#ff0}como{/color}"
    consola "{color=#f0f}#Raiz cuadrada de 25{/color}\nimport math as m\nm.sqrt(25)\n5.0"
    h "También podemos dar importar la funcion sqrt del módulo math usando las palabras reservadas {color=#ff0}from{/color} que en inglés significa {color=#ff0}desde{/color}"
    consola "{color=#f0f}#Raiz cuadrada de 25{/color}\nfrom math import sqrt\nsqrt(25)\n5.0"
    h "Tambien podemos usar ambas palabras reservadas"
    consola "{color=#f0f}#Raiz cuadrada de 25{/color}\nfrom math import sqrt as raizCuadrada\nraizCuadrada(25)\n5.0"
    h "Podemos calcularlo de otra manera, teniendo en cuenta que la raíz cuadrada de un número es lo mismo que elevarlo a la 1/2\nla raíz cúbica es lo mismo que elevarlo a la 1/3, la cuarta a la 1/4, etc"
    h "Sin necesidad de importar ningún módulo podemos calcular la raíz cuadrada de 25 así"
    consola "{color=#f0f}#Raiz cuadrada de 25{/color}\nhalf=1.0/2.0\n25**half\n5.0"
    h "El objetivo del logaritmo es el cálculo del exponente si sabemos la base y la potencia"
    h "Si sabemos de 4*4, o 4**2 es 16, entonces el logaritmo de 16 con base 4 es 2"
    h "En Python, para calcular el logaritmo debemos importar el método log del módulo math para calcular el logaritmo"
    consola "{color=#f0f}#Para calcular el logaritmo de 16 con base 2{/color}\nimport math\nmath.log(16,2)\n4.0"
    hide text
    $ error=""
    $ counter=0
    $ respuesta=10
label q15:
    $ encabezado="Calcule usando Python:\n"
    $ encabezados = ["Siete elevado a la quinta potencia", "La raíz cuadrada de 64 usando el módulo math", "La raíz cuadrada de 49 usando un flotante como exponente"]
    $ Menus = [ ["7*5", "7**5", "7***5"],
                ["import math\nmath(64,2)", "import math\nsqrt(64)", "from math import sqrt as Rcuadrada\nRcuadrada(64)"],
                ["49**0.5", "0.5**49", "float(49)**2"]]
    $ claves =[1,2,0]
    
    if respuesta==10:
        pass
    elif respuesta == claves[counter] and counter < 3:
        $counter += 1
    else:
        $error="¡Eso no es correcto!"
    if error:
        h "[error]"
        $error=""
    if counter <=3 and not error:
        if counter < 3 :
            h "CORRECTO"
            h "Vamos por el siguiente reto"
        else:
            h "Exacto, has concluido este ejercicio"
            jump n12
    $encabezado += encabezados [counter]
    $Menu1=Menus[counter][0]
    $Menu2=Menus[counter][1]
    $Menu3=Menus[counter][2]
    menu:
        consola "[encabezado]"
        "[Menu1]":
            $ respuesta = 0
            jump q15
        "[Menu2]":
            $ respuesta = 1
            jump q15
        "[Menu3]":
            $ respuesta = 2
            jump q15
label n12: 
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "Una utilidad práctica de la exponenciación es el cálculo de los lados de un triángulo rectángulo basado en el teorema de Pitágoras"
    h "El teorema de Pitágoras se utiliza para calcular distancias entre 2 puntos en un plano"
    h 'Si las distancias son menores a un valor determinado, tenemos una "colisión"'
    h "El teorema de Pitágoras tiene que ver también como los conceptos de conversión materia y energía propuesto por la Teoría de la Relatividad de Einstein o la teoría de la formación de antimateria"
    h "Para recordar, los triangulos tienen 3 lados y 3 ángulos"
    h "La suma de los 3 ángulos de un triángulo (siempre que esté en un plano) da por resultado 180 grados"
    h "Cuando uno de sus ángulos es recto, es decir que mide 90 grados, tenemos un triángulo rectángulo y podemos aplicar el teorema de Pitágoras"
    h "Los triángulos rectángulos su lado más largo opuesto al ángulo recto y éste se denomina hipotenusa (la vamos a llamar c)"
    h "Los otros dos lados más cortos del triángulo (que forman el triángulo rectángulo) se denominan catetos (los vamos a llamar a y b)"
    h "El teorema de Pitágoras establece que la hipotenusa al cuadrado es la suma de las cuadrados de los catetos"
    h "¡Qué enredo!"
    h "#El Teorema de Pitagoras luce así en codigo Python\n c=(a**2+b**2)**.5"
    h "¡Epa! ¿Y esos paréntesis?"
    h "Tranquilo esos paréntesis son para explicar otro concepto llamado la prodecencia de los operadores aritméticos"
    h "Las operaciones aritméticas se realizan en este órden: primero cualquier cosa que esté paréntesis, luego las potencias, luego las multiplicaciones y divisiones; y finalmente las sumas y las restas"
    h "Al escribir {color=#ff0}c=(a**2+b**2)**.5{/color} estamos primero elevando al cuadrado a y b"
    h "luego realizando la suma de esos cuadrados y finalmente sacando la raíz cuadrada a esa suma (es decir elevando por 0.5)"
    hide text
    $error=""
label q16:
    h "Vamos a ver un {color=#ff0}lienzo{/color}, en inglés llamado {color=#ff0}canvas{/color}"
    h "En la implementación Python 'Pygame' y en las páginas web, el lienzo (o canvas) representa un sistema de coordenadas con el origen en la esquina superior izquierda"
    menu:
        "Si tenemos una variable x que contiene la distancia de un objeto O en milimetros desde el borde izquierdo del lienzo\ny una variable y que contiene la distancia en milimetros desde el borde superior del lienzo\n¿Cual de estos códigos Python representa la variable d que contiene la distancia entre el objeto y la esquina superior izquierda?"
        "d=(y**2+x**2)**.5":
            h "¡Correcto!"
        "d=(x**2+y**2)**5":
            h "¡Eso no es correcto!"
            jump q16
        "d=(x**2+y**2)**.5+O":
            h "¡Eso no es correcto!"
            jump q16
label n13:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "Creo que me he emociado con los operadores... ¡pero aun no acabo!"
    h "Vamos a imaginar que estamos jugando cualquier video juego... Mario Bros, cualquier shooter, Candy Crush, etc"
    h "A medida que hacemos ciertas acciones, nuestro puntaje, vidas o el tiempo restante cambian"
    h "En el caso de Mario Bros., al tocar una moneda nuestro contador de monedas sube un punto."
    h "En ese mismo juego, al tocarnos un enemigo estando chiquitos perdemos una vida y el contador de vidas baja una unidad (Si teníamos 3 vidas ahora tenemos 2)"
    h "En ese y muchos otros video juegos, hay una serie de variables que tienen ese comportamiento debido que son escudriñadas por operadores de incremento y decremento" 
    h "Python hay 2 operadores de incremento y 2 de decremento"
    h "Estos operadores (a diferencia del de asignación) requiere que dichas variables existan"
    h "De lo contrario tenemos un error de sintaxis"
    h "Una vez que creamos una variable la podemos modificar con estos operadores"
    h "En el caso del operador aditivo de incremento {color=#ff0}+={/color}, el valor de la variable de la izquierda sube el número de unidades del número de la derecha del operador"
    consola "x=5\nx += 2\nx\n7\nx += 2\nx\n9"
    h "En operador de decremento aditivo, {color=#ff0}-={/color}, es similar al de incremento, pero en lugar de subir el valor de la variable, lo baja"
    h "vidas=3\nvidas -= 1\nvidas\n2\nvidas -= 1\nvidas\n1"
    h "En operador de incremento multiplicativo, {color=#ff0}*={/color}, es similar al de incremento aditivo, pero en lugar de sumar el valor de la variable, lo sube multiplicando por el valor de la derecha"
    consola "vidas=5\nvidas *= 2\nvidas\n10\nvidas *= 4\nvidas\n40"
    h "En operador de decremento multiplicativo, {color=#ff0}/={/color}, es similar al de incremento multiplicativo, pero en lugar de multiplicar el valor de la variable, lo disminuye dividiendo por el valor de la derecha"
    consola "municiones=42\nmuniciones /= 5\nmuniciones\n8\nmuniciones /= 2\nmuniciones\n4"
    h "Vamos a ver el siguiente ejercicio"
    hide text
    $error=""
label q17:
    if error:
        h "[error]"
        $error=""
    menu:
        "Calcule el valor de la raciones despues de ejecutar el codigo\nraciones=25\nraciones /= 7\nraciones"
        "Error de compilacion":
            $ error= "No veo ningun error en ese código"
            jump q17
        "3":
            h "Correcto, al dividir entre 2 enteros, obtenemos otro entero, es decir 25/7=3"
        "3.5714285714285716":
            $error="¡Qué número más enredado!, esa no es la respuesta correcta"
            jump q17
label n14:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    
    h "Antes de terminar con estos dichosos operadores aritméticos, voy a habar de la {color=ff0}coerción{/color} de variables"
    h "Había dicho anteriormente que el resultado de uno o más operadores aritméticos es un número entero o flotante"
    h "También había dicho que existen 2 tipos variable numéricas en Python (int y el float) y otros 2 tipos que son la cadena (string) y el boolean"
    h "Si aplicamos cualquiera de estos operadores entre un número y una cadena (string) vamos a tener un error de compilación (así de simple)"
    h "Si tenemos operaciones aritméticas entre un enteros y por lo menos un boolean, el boolean se convierte o {color=#ff0}coerciona{/color} a un entero de valor 1 si es True y 0 si es False"
    h "Si tenemos operaciones aritméticas con por lo menos un número flotante y por lo menos un boolean, el boolean se {color=#ff0}coerciona{/color} a un flotante de valor 1.0 si es True y 0.0 si es False"
    h "#Por ejemplo\n2+2+True+False\n5"
    h "#Otro ejemplo\n2+2+True+False*3.+234**False\n6.0"
    h "Vamos a ver otro ejercicio"
    hide text
    $error=""
label q18:
    if error:
        h "[error]"
        $error=""
    menu:
        "Calcule el valor de la raciones despues de ejecutar el codigo\n14./False"
        "Error de compilacion":
            h "¡Excelente! esa expresión ocasiona una división entre cero, el cual es inaceptable"
        "14":
            $error= "Eso es incorrecto"
            jump q18
        "0":
            $error="¡Qué número más enredado!, esa no es la respuesta correcta"
            jump q18
label n15:
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos y de asignación{/color}{/size}" at top
    h "Al fin acabamos con esos operadores aritméticos y de asignación"
    h "Vamos a ver 2 operadores que solo sirven para cadenas (strings) que el operador de concatenación y de formato"
    h "El operador de concatenación es {color=#ff0}+{/color}, el cual es idéntico al de la suma, pero cuando está entre strings va a concatenarlos, es decir va a unir dos o más cadenas hacer una cadena más largo"
    consola '"Hola "+ "mundo!"\n"Hola mundo"'
    consola '"Hola, "+"¿cómo "+ "estás?"\n"Hola, ¿cómo estás?"'
    consola 'saludo="Hola, "\nnombre="Pepe"\nsaludo+nombre\n"Hola, Pepe"'
    h 'El otro operador es la "interpolación" de variables'
    h "Veamos este ejemplo"
    consola 'pregunta="¿Cuánto es 2+2?"\nrespuesta=4\npregunta+respuesta\nTraceback (most recent call last):\n  File "\<stdin\>", line 1, in \<module\>\nTypeError: cannot concatenate \'str\' and \'int\' objects'
    h "Para evitar estos problemas, podemos hacer una {color=#ff0}interpolación{/color} de variables"
    consola 'repuesta=4\n"2+2 es \%s" respuesta\n"2+2 es 4"'
    $error=""
    $ counter = 9
label q19:
    
    $ expresiones = ['1+1', '"1"+1', '"1"+"False"', "True + 2"]
    $ respuestas = [3,2,4,1]
    if counter==9:
        python:
            counter=0
            encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[0]
            
    else:
        #$encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[counter]
        if check == respuestas[counter]:
            h "Eso es correcto"
            $counter += 1
            if counter==4:
                h "Has completado esta actividad"
                $ del expresiones
                $ del respuestas
                $ del counter
                jump n16
            else:
                $encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[counter]
        else:
             h "[error]"
    menu:
        "[encabezado]"
        '3':
            $check=1
            jump q19
        "Error de compilación":
            $check=2
            jump q19
        "2":
            $check=3
            jump q19
        "1False":
            $check=4
            jump q19
label n16:
    show text "{size=40}{color=#000}Capítulo cinco\n\n\nLos operadores lógicos y el control de flujo{/color}{/size}" at top
    h "Vamos a hablar de las variables y operadores boolean o lógicas y del control de flujo"
    h "Antes de proseguir voy a hablar del cambio de tipo de las variables"
    h "Las variables tipo cadena {color=#f00}NO{/color} se pueden convertir en tipo numéricas, a menos que la cadena contenga números sin espacios o que contenga uno o más numeros y un punto"
    consola "{color=#f0f}#Esto no está permitido{/color}\nint(\"hola\")\nTraceback (most recent call last):\n  File \"\<stdin\>\" in \<module\>\nValueError: invalid literal for int() with base 10: 'hola'"
    consola "{color=#f0f}#Esto tampoco está permitido{/color}\nfloat(\"hola\")\nTraceback (most recent call last):\n  File \"\<stdin\>\" in \<module\>\nValueError: could not convert string to float"
    consola "{color=#f0f}#Pero sí está permitido{/color}\nint(\"12\")\n12"
    consola "{color=#f0f}#Y esto también está permitido{/color}\nfloat(\"12.8\")\n12.8"
    h "Las variables numéricas pueden convertirse en cadenas sin ningún inconveniente"
    consola "{color=#f0f}#Conversión de flotante a cadena{/color}\nstr(12.)\n\'12.0'"
    consola "{color=#f0f}#Conversión de entero a cadena{/color}\nstr(567)\n\'567'"
    h "No hay ningún tipo de restricción para convertir de cualquier tipo a boolean"
    h "Cualesquiera que sea el valor de la variable, el boolean siempre será cierto, es decir ({color=#ff0}True{/color})"
    h "Sin embargo, al coercionar a boolean, el resultado será falso es decir ({color=#ff0}False{/color}),si la variable es de tipo {color=#ff0}None{/color} (que es un tipo de variable de Python que no contiene nada),\nuna variable numérica con el {color=#ff0}0{/color} \no sea un cadena vacía, es decir {color=#ff0}''{/color} o {color=#ff0}\"\"{/color}"
    consola "{color=f0f}#Algunos ejemplos{/color}\nbool(2)\nTrue\nbool(145.3)\nTrue\nbool(\"¿Cómo estás?\")\nTrue"
    consola "{color=f0f}#Algunos ejemplos{/color}\nbool(None)\nFalse\nbool(5-5)\nFalse\nbool(\"\")\nFalse"
    h "Ahora vamos a ver un par de ejercicios"
    hide text
    python:
        menus=[['True', 'False', 'None'],
                    ['0', '1', '45']]
        counter=9
        check=None
        expresiones=['bool(15)', 'int(bool(45))', 'bool(65*0)']
        respuestas= ['True', '1', 'False']
label q20:
    if counter==9:
        $counter=0
    if check:
        if check == respuestas[counter]:
            h "CORRECTO!"
            $counter += 1
        
    if counter == 3:
        python:
            del counter
            del expresiones
            del menus
            del respuestas
            del encabezado
        h "Has completado esta actividad"
        jump n17
            
    else:
        $encabezado = "¿Cuál es el valor de las siguientes expresiones?\n" +  expresiones [counter]
        if counter != 1 :
            python:
                menu1 = menus[0][0]
                menu2 = menus[0][1]
                menu3 = menus[0][2]
        else:
            python:
                menu1 = menus[1][0]
                menu2 = menus[1][1]
                menu3 = menus[1][2]
    menu:
        "[encabezado]"
        '[menu1]':
            $check=menu1
            jump q20
        '[menu2]':
            $check=menu2
            jump q20
        '[menu3]':
            $check=menu3
            jump q20
label n17:
    show text "{size=40}{color=#000}Capítulo cinco\n\n\nLos operadores lógicos y el control de flujo{/color}{/size}" at top
    h "Es importante el control de flujo, que tiene que ver con la toma de decisiones una vez que un evento cambia el valor de una variable"
    h "Respuesta a preguntas como ¿qué ocurre cuando el medidor de aceite de un carro llega a cierto nivel? o ¿qué ocurre cuando se obtiene un objeto en un videojuego? son preguntas que tienen que ver con el {color=#ff0}control de flujo{/color}"
    h "La idea del control de flujo es valorar diversas acciones a tomar basado en los cambios de una o varias variables"
    h "Por eso es indispensable conocer a los uso de operadores lógicos en mayor detalle"
    h 'Hay ciertos operadores que comparan el valor de 2 variables:\n"es igual a" {color=#ff0}=={/color}\n"no es igual a" {color=#ff0}!={/color} o también {color=#ff0}\<\>{/color}\n"es mayor que" {color=#ff0}>{/color}\n"es menor que" {color=#ff0}<{/color}\n"es mayor o igual a" {color=#ff0}>={/color}\n"es menor o igual a" {color=#ff0}<=\n{/color}'
    h "En variables numéricas es creo que obvio"
    consola "{color=#f0f}#Es bastante claro como funciona \"es igual a\" con números{/color}\n2{color=#ff0}=={/color}2\nTrue\n5{color=#ff0}=={/color}4\nFalse"
    consola "{color=#f0f}#Es bastante claro como funciona \"no es igual a\" con números{/color}\n2{color=#ff0}!=2{/color}\nFalse\n5{color=#ff0}!={/color}4\nTrue"
    consola "{color=#f0f}#Aquí vemos al \"mayor que\" con números{/color}\n2{color=#ff0}>{/color}2\nFalse\n5{color=#ff0}>{/color}4\nTrue"
    consola "{color=#f0f}#y acá vemos al \"menor que\" con números{/color}\n2{color=#ff0}<{/color}2\nFalse\n5{color=#ff0}<{/color}4\nFalse"
    consola "{color=#f0f}#seguimos con el \"mayor o igual a\" con números{/color}\n2{color=#ff0}>={/color}2\nTrue\n5{color=#ff0}>={/color}4\nTrue"
    consola "{color=#f0f}#y terminamos con el \"menor o igual a\" con números{/color}\n2{color=#ff0}<={/color}2\nTrue\n5{color=#ff0}<={/color}4\nFalse"
    h 'En el caso de las variables o valores tipo cadena, es muy usado los operadores "igual a" {color=#ff0}=={/color} y "no es igual a" {color=#ff0}!={/color}'
    h "Aunque es posible usar otros operadores lógicos de comparación en las cadenas, usualmente no es muy práctico"
    consola "{color=#f0f}#Así funciona \"es igual a\" en variables tipo cadenas{/color}\n'hola'{color=#ff0}=={/color}\"hola\"\nTrue\n'hola'{color=#ff0}=={/color}'mundo'\nFalse"
    consola "{color=#f0f}#Pero así funciona \"no es igual a\" en variables tipo cadenas{/color}\n'hola'{color=#ff0}!={/color}\"hola\"\nFalse\n'hola'{color=#ff0}!={/color}'mundo'\nTrue"
    h "Lo importante de estos operadores es que {color=#ff0}siempre{/color} resultan en un valor lógico"
    h "Vamos a ver un ejercicio"
    hide text
    python:
        menus=['True', 'False', 'None']
                    
        counter=9
        check=None
        expresiones=['4>8', "int('12')==12.", 'str(24)!= "24.0"']
        respuestas= ['False', 'True', 'False']
        encabezado=""
        error=""
label q21:
    if counter==9:
        $counter=0
    if check:
        if check == respuestas[counter]:
            h "CORRECTO!"
            $counter += 1
        else:
            $error="Es INCORRECTO!"
        
        if counter == 3:
            python:
                del counter
                del expresiones
                del menus
                del respuestas
                del encabezado
            h "Has completado esta actividad"
            jump n18
                
        else:
            
            
            python:
                menu1=menus[0]
                menu2=menus[1]
                menu3=menus[2]
    if error:
        h "[error]"
        $ error =""
    $encabezado = "¿Cuál es el valor de las siguientes expresiones?\n" +  expresiones [counter]
    menu:
        "[encabezado]"
        '[menu1]':
            $check=menu1
            jump q21
        '[menu2]':
            $check=menu2
            jump q21
        '[menu3]':
            $check=menu3
            jump q21
    
label n18:
    show text "{size=40}{color=#000}Capítulo cinco\n\n\nLos operadores lógicos y el control de flujo{/color}{/size}" at top
    h "Antes de proseguir debemos recordar los operadores aritmétcos: {color=#ff0}+{/color}, {color=#ff0}-{/color}, {color=#ff0}*{/color}, {color=#ff0}/{/color} y {color=#ff0}\%{/color}"
    h "Cualquier operación con estos operadores, Python la va a resolver {color=#ff0}antes{/color} de comparar los resultados"
    consola "{color=#f0f}Veamos este concepto{/color}\n3 + 5 > 2 - 1 {color=#f0f}#Es decir 8 > 1 que es cierto{/color} \nTrue"
    consola "{color=#f0f}Veamos otro ejemplo{/color}\n12 * 2 >= 20 + 4 {color=#f0f}#Es decir 24 >= 24 que tambien es cierto{/color} \nTrue"
    h "Vamos a ver 3 operadores lógicos más: {color=#ff0}not{/color}, {color=#ff0}and{/color} y {color=#ff0}or{/color}"
    h "{color=#ff0}not{/color} es el único operador que solo toma un parámetro que es lo que está a derecha"
    h "El operador {color=#ff0}not{/color} hace una coerción a boolean de lo que que tenga a su lado (si no es un boolean) y luego le cambia el valor de {color=#ff0}True{/color} a {color=#ff0}False{/color} o de {color=#ff0}False{/color} a {color=#ff0}True{/color}"
    h "Veamos unos ejemplos"
    consola "{color=#f0f}#Veamos como funciona el operador {color=#ff0}not{/color}{/color}\nnot True\nFalse\nnot False\nTrue"
    consola "{color=#f0f}#Veamos operador {color=#ff0}not{/color} haciendo coerción del valores numéricos{/color}\nbool(37.5)\nTrue\nnot 37.5\nFalse"
    consola "{color=#f0f}#Veamos operador {color=#ff0}not{/color} haciendo coerción del valor None{/color}\nbool(None)\nFalse\nnot None\nTrue"
    consola "{color=#f0f}#Veamos operador {color=#ff0}not{/color} haciendo coerción una variable tipo cadena{/color}\nhola=\"Hola mundo\"\nbool(hola)\nTrue\nnot hola\nFalse"
    consola "{color=#f0f}#Veamos operador {color=#ff0}not{/color} haciendo coerción una variable tipo cadena vacía{/color}\nnada=\"\"\nbool(nada)\nFalse\nnot nada\nTrue"
    h "El operador {color=#ff0}and{/color} compara si se coloca entre 2 valores booleanos, devuelve True cuando ambos son True (o ciertos)"
    consola "{color=#f0f}#Veamos como funciona el operador {color=#ff0}and{/color}{/color}\nTrue and True\nTrue\nTrue and False\nFalse"
    h "El operador {color=#ff0}and{/color} además compara si se coloca entre 1 valor booleano y otro de otro tipo, devuelve True cuando el booleano es True y el otro valor puede ser coercionado a True"
    consola "{color=#f0f}#Veamos como funciona el operador {color=#ff0}and{/color} en otro ejemplo{/color}\nTrue and 3\nTrue\nTrue and \"\" {color=#ff0}#Recordemos que \"\" se coerciona a False{/color}\nFalse\nFalse and 2\nFalse"
    h "Vamos a combinar los operadores {color=#ff0}not{/color} y {color=#ff0}and{/color}"
    consola "{color=#f0f}#Otro ejemplo de los operadores {color=#ff0}and{/color} y {color=#ff0}not{/color}{/color} combinados\nnot True and True\nFalse\nTrue and not False\nTrue"
    h 'Si el operador and aparece entre 2 valores o variables que no son boolean, va a retornar el valor a su derecha a menos que sea 0, None o ""'
    h "Esto es interesante saber, pero no muy útil"
    h "Ahora vamos a hablar del operador {color=#ff0}or"
    h "El operador {color=#ff0}or{/color}, si se coloca entre 2 valores booleanos, devuelve True cuando uno de los dos es True (o ciertos)"
    consola "{color=#f0f}#Veamos como funciona el operador {color=#ff0}or{/color}{/color}\nTrue or True\nTrue\nTrue or False\nTrue"
    h "Si colocamos el operador además compara si se coloca entre 1 valor booleano y otro de otro tipo, se devuelve True cuando el booleano es True o el otro valor puede ser coercionado a True"
    consola "{color=#f0f}#Veamos como funciona el operador {color=#ff0}or{/color} en otro ejemplo{/color}\nTrue or 3 {color=#f0f}#Recordemos que 3 se coerciona a True{/color}\nTrue\nTrue or \"\" {color=#f0f}#Recordemos que {color=#ff0}\"\"{/color} se coerciona a False{/color}\nTrue\nFalse or 2{color=#f0f}#Recordemos que 2 se coerciona a True{/color}\nTrue"
    h "Vamos a trabajar con algunos ejemplos"
    hide text
    python:
                    
        counter=9
        check=None
        expresiones=['True and False or True', "False or not 3 >= 8", 'not str(24)!= "24.0" and not 6 == 18/3']
        respuestas= ['True', 'True', 'False']
        encabezado=""
        error=""
label q22a:
    if counter==9:
        $counter=0
    if check:
        if check == respuestas[counter]:
            h "CORRECTO!"
            $counter += 1
        else:
            $error="Es INCORRECTO!"
        
        if counter == 3:
            python:
                del counter
                del expresiones
               # del menus
                del respuestas
                del encabezado
            h "Has completado esta actividad"
            jump n19
                
    if error:
        h "[error]"
        $ error =""
    $encabezado = "¿Cuál es el valor de las siguientes expresiones?\n" +  expresiones [counter]
    menu:
        "[encabezado]"
        'True':
            $check="True"
            jump q22a
        'False':
            $check="False"
            jump q22a
        'None':
            $check='None'
            jump q22a

label n19:
    show text "{size=40}{color=#000}Capítulo cinco\n\n\nLos operadores lógicos y el control de flujo{/color}{/size}" at top
    h "Antes de entrar de lleno a hablar del control de flujo, les tengo que hablar del operador lógico {color=#ff0}in{/color}"
    h 'El operador {color=#ff0}in{/color} es un operador lógico especial que nos permite hablar de las 4 "estructuras de datos" de Python: la lista, el tuplo, el diccionario y el conjunto'
    h "Las estructuras de datos son variables que pueden tener uno o más valores dentro de ellas de cualquier tipo"
    h "Para accesar un valor dentro, en el caso de la lista y del tuplo se requiere de un indice y en caso del diccionario una clave"
    h "Hay 2 formas de crear una lista, podemos crear una lista vacía usando list(), o metiendo los elementos que querramos con un par de corchetes cuadradros \[\] separados por comas"
    consola "{color=#f0f}#Vamos a crear dos listas vacía{/color}\nlistaVacía1=list()\nlistaVacía2=\[\]"
    consola '{color=#f0f}#Vamos a crear una lista de profesores{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi", "Sir. Mark Thackeray"\]'
    h "Podemos acceder a un elemento de la lista usando los índices. Los índices son números que indican la posición del elemento"
    h "Los índices positivos indican la posición de izquierda a derecha empezando desde 0"
    consola '{color=#f0f}#Veamos como trabajan los indices{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray"\]\nProfeDelChavo=Profesores\[0\]\nProfeDelGoku=Profesores\[1\]\nProfeDelChavo\n"Profesor Jirafales"\nProfeDelGoku\n"Maestro Rochi"'
    h "Los índices negativos indican la posición de derecha a izquierda a derecha empezando desde -1"
    consola '{color=#f0f}#Veamos como trabajan los indices negativos{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray"\]\nProfeDelChavo=Profesores\[-3\]\nProfeDelGoku=Profesores\[-2\]\nProfeDelChavo\n"Profesor Jirafales"\nProfeDelGoku\n"Maestro Rochi"'
    h "Para crear un tuplo, simplemente ponemos todos los elementos uno tras otro separados por comas y encerrados en un par de paréntesis"
    consola '{color=#f0f}#Vamos a crear una tuplo de profesores{/color}\nProfesores=("Profesor Jirafales", "Maestro Rochi", "Sir. Mark Thackeray")'
    h "Los índices en los tuplos funcionan de la misma manera que en las listas"
    consola '{color=#f0f}#Veamos como trabajan los indices en un tuplo{/color}\nProfesores=("Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Hedley Quintana")\nProfeDelChavo=Profesores\[0\]\nProfeDelGoku=Profesores\[-3\]\nProfeDelChavo\n"Profesor Jirafales"\nProfeDelGoku\n"Maestro Rochi"'
    h "Podemos seleccionar varios elementos de una lista o tuplo mediante el {color=#ff0}corte{/color} de los elementos"
    h "El {color=#ff0}corte{/color} de los elementos se realiza mediante un rango de índices que van desde el primer elemento hasta el previo al último,\nveamos un ejemplo"
    consola '{color=#f0f}#Veamos como trabajan los cortes{/color}\nProfesores=("Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Hedley Quintana")\nProfesComicos=Profesores\[0:2\] {color=#f0f}#Esta lista selecciona los índices de 0 al 1, el 2 NO está incluido{/color}\nProfesComicos\n("Profesor Jirafales", "Maestro Rochi")'
    h "La diferencia entre el tuplo y la lista, es que el tuplo es {color=#ff0}inmutable{/color} y la lista no"
    h "El tuplo una vez creado no se puede modificar, pero la lista sí. Aunque Python le permite a una variable tipo tuplo ser reemplazado por otro tuplo u otro tipo de variable"
    h "A la lista le puede añadir, modificar o quitar elementos una vez creada"
    h "Para modificar un elemento de una lista, basta y sobra con asignarle el valor al elemento usando el índice"
    consola '{color=#f0f}#Veamos cambiar el valor de "Maestro Rochi" a "Mr Rochi"{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray"\]\nProfesores\[1\]="Mr. Rochi"\nProfesores\n\["Profesor Jirafales", "Mr. Rochi", "Sir. Mark Thackeray"\]'
    h "Para añadir un elemento al final de la lista usamos la función append.\nPara usar esta función ponemos el nombre de variable con la lista, un punto, luego la palabra append y finalmente entre paréntesis lo que queremos añadir al final de la lista"
    consola '{color=#f0f}#Veamos añadir al profesor "Saitama al final de la lista"{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray"\]\nProfesores.append("Saitama)"\nProfesores\[-1\]\n"Saitama"'
    h "La función pop sin argumentos (lo que está entre paréntesis está vacío) elimina el último elemento de la lista y devuelve dicho elemento"
    h "Podemos eliminar de la lista "
    consola '{color=#f0f}#Veamos eliminar al profesor "Saitama del final de la lista"{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Saitama"\]\nProfesores.pop()"\nProfesores\[-1\]\n"Sir. Mark Thackeray"'
    consola '{color=#f0f}#Podemos con la función pop guardar el elemento eliminado en una variable"{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Saitama"\]\nElMasPoderoso = Profesores.pop()"\nProfesores\[-1\]\n"Sir. Mark Thackeray"\nElMasPoderoso\n"Saitama"'
    h "La función pop con un argumentos numérico elimina el elemento de la lista con ese índice y devuelve dicho elemento"
    consola '{color=#f0f}#Podemos con la función pop con argumento"{/color}\nProfesores=\["Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Saitama"\]\nMeCaeMal = Profesores.pop(0)"\nProfesores\[0\]\n"Maestro Rochi"'
    h "Podemos saber además cuantos elementos tiene una lista o un tuplo con la funcion len y entre paréntesis el nombre de la lista"
    consola '{color=#f0f}#Vamos a usar la función len"{/color}\nProfesores=("Profesor Jirafales", "Maestro Rochi",\n"Sir. Mark Thackeray", "Saitama")\nlen(Profesores)\n4'
    h "El diccionario no tiene ningún orden al ser invocado, pero en lugar de índices, usa {color=#ff0}claves{/color} de tipo cadena para seleccionar y al igual que la lista sus elementos pueden ser modificados"
    h "En el diccionario, las claves son {color=#ff0}ÚNICAS{/color} y son la única manera de acceder a los elementos del mismo"
    h "El diccionario se puede crear mediante la función dict(), o mediante una serie de claves y valores (la clave separadas del valor mediante dos puntos {color=#ff0}:{/color}) encerrados por corchetes cursivos"
    consola '{color=#f0f}#Vamos a crear un diccionario{/color}\nnombreDeAsientosVacío=dict()\nnombreDeAsientos=\{"Ana": "A1", "Pepe":"C52", "Juan":"W15"\}\nnombreDeAsientos\["Ana"\]\n"A1"'
    h "Y finalmente, el conjunto en inglés {color=#ff0}set{/color}, es una estructura de datos la cual contiene elementos con valores repetidos"
    h "Son bastante dificiles de usar, pero los conjuntos NOS GARANTIZAN que ningun valor puede estar REPETIDO"
    consola '{color=#f0f}#Vamos a crear un conjunto{/color}\nconjuntoDeIds=set(\["2A", 2, "3B", 2, 5, 8\])\nconjuntoDeIds\nset(\["2A", "3B", 2, 5, 8\])'
    h "Ah! finalmente el operador {color=#ff0}in{/color} simplemente indica si un valor de un elemento está o no presente un estructura de datos (excepto en el diccionario) y de ser así devuelve True y sino es así devuelve False"
    h "En los diccionarios, el operador in devuelve cierto o {color=#ff0}True{/color} siempre y cuando que la cadena sea parte de una clave del diccionario"
    consola '{color=#f0f}#Vamos a ver el operador in en un diccionario{/color}\nnombreDeAsientos=\{"Ana": "A1", "Pepe":"C52", "Juan":"W15"\}\n"Ana" in nombreDeAsientos\nFalse {color=#ff0}#Ana es un clave del diccionario, es una clave{/color}\n"A1" in nombreDeAsientos\nFalse'
    consola '{color=#f0f}#Vamos a ver el operador in{/color}\nconjuntoDeIds=set(\["2A", 2, "3B", 2, 5, 8\])\n"2a" in conjuntoDeIds\nFalse\n\n"2A" in conjuntoDeIds\nTrue'
    h "Vamos a repasar un poco de lo aprendido"
    hide text
    python:
        del menu1, menu2, menu3
        menus=[['None', '0', '1'],
               ['2', '4', '6'],
               ['1','3','5']]
        counter=9
        check=None
        expresiones=['a=[]\nlen(a)', "a=[[1,2,3],[4,5,6]]\na[1][0]", 'a=([1,2,3],[4,5,6])\na[0][2]']
        respuestas= ['0', '4', '3']
        encabezado=""
        error=""
label q22:
    if counter==9:
        $counter=0
    if check:
        if check == respuestas[counter]:
            h "CORRECTO!"
            $counter += 1
        else:
            $error="Es INCORRECTO!"
        
        if counter == 3:
            python:
                del counter
                del expresiones
                del menus
                del respuestas
                del encabezado
            h "Has completado esta actividad"
            jump n24
                
    python:
        menu1=menus[counter][0]
        menu2=menus[counter][1]
        menu3=menus[counter][2]
    if error:
        h "[error]"
        $ error =""
    $encabezado = "¿Cuál es el valor de las siguientes expresiones?\n" +  expresiones [counter]
    menu:
        "[encabezado]"
        '[menu1]':
            $check=menu1
            jump q22
        '[menu2]':
            $check=menu2
            jump q22
        '[menu3]':
            $check=menu3
            jump q22
label n24:    
    h "Ahora si vamos a entrar con el control de flujo, para ello tenemos 4 operadores {color=#ff0}if{/color}, {color=#ff0}else{/color}, {color=#ff0}elif{/color} y {color=#ff0}while{/color}"
    h "Ahora vamos a ver como funciona el control de flujo"
    h "Primero imaginemos que manejamos un carro y nos encontramos un semáforo en rojo"
    h "De repente la luz cambia a verde, lo que indica que podemos avanzar"
    h "Dentro de un programa una {color=#ff0}toma de decisión{/color} se ejecuta automáticamente cuando una o más variables cambian de estado"
    h "El control de flujo, implica una serie de acción que ocurren cuando una variable toma un determinado valor"
    h "El control de flujo en Python se realiza mediante {color=#ff0}bloques{/color} cuando una {color=#ff0}condición{/color} es {color=#ff0}cierta{/color}"
    h "Las palabras reservadas que delimitan el {color=#ff0}control de flujo{/color} son {color=#ff0}if{/color}, {color=#ff0}else{/color}, {color=#ff0}elif{/color} y {color=#ff0}while{/color}"
    h "Comenzamos por la palabra reservada {color=#ff0}if{/color} que significa en español {color=#ff0}si{/color}"
    h "Hay dos formas de crear un control de flujo con {color=#ff0}if{/color}: con una línea o con un bloque"
    h "Para crear una línea, escribimos la palabra reservada {color=#ff0}if{/color} seguida por una condición (que debe ser cierta para que se ejecute la línea)\nluego dos puntos {color=#ff0}seguido de la acción a ejecutar{/color}"
    h "Si la condición no se cumple, el código despues de los dos puntos {color=#ff0}:{/color} no se ejecuta"
    consola "{color=#f0f}#Versión Python 2 (note que el argumento de print NO está encerrado en paréntesis)\ncomo a >20 es falso, el código no se ejecuta{/color}\na=14\nb=2\nif a>20: print b"
    consola "{color=#f0f}#Versión Python 2 (note que el argumento de print NO está encerrado en paréntesis), como a >20 es cierto, el código se ejecuta{/color}\na=24\nb=2\nif a>20: print b\n2"
    consola "{color=#f0f}#Versión Python 3 (note que el argumento de print está encerrado en paréntesis), como a >20 es falso, el código no se ejecuta{/color}\na=14\nb=2\nif a>20: print (b)"
    consola "{color=#f0f}#Versión Python 3 (note que el argumento de print está encerrado en paréntesis), como a >20 es cierto, el código se ejecuta{/color}\na=24\nb=2\nif a>20: print (b)\n2"
    h "Si queremos ejecutar más de una línea necesitamos un {color=#ff0}bloque{/color}"
    h "El bloque es una serie de líneas que tienen {color=#ff0}sangría{/color} adicicional despues de la sentencia que inicia con if"
    h "El bloque termina en la última línea con {color=#ff0}sangría{/color}"
    h "En este tutorial he usado bloques {color=#ff0}if{/color} para valorar si sus respuestas son correctas o no"
    h "Pueden ver esto en la página github de este proyecto{a=https://github.com/HedleyPty/AprendiendoPython} Repositorio GitHub{/a} en las líneas 142 a 180\ntambién puedes ver los bloques menu de Ren'py donde verifico las respuestas"
    h "Al contestar una respuesta correcta se compara el valor de la variable con su respusesta con un elemento de una lista que contiene las respuestas correctas"
    consola "{color=#f0f}#Esto ocurre cada vez que responden en los ejercicios{/color}\nif check == respuestas\[counter\]:\n\ \ \ \ counter += 1\n\ \ \ \ if counter ==3:\n\ \ \ \ {color=#f0f}#La función {color=#ff0}jump{/color} permite pasar al siguiente capítulo en Ren\'py{/color}\n\ \ \ \ jump proxCapitulo "
    h "El operador {color=#ff0}while{/color} no es en verdad un control de flujo sino un {color=#ff0}bucle{/color}, en inglés {color=#ff0}loop{/color}"
    h "Los bucles son operaciones que se repiten siempre y cuando una condición sea cierta"
    h "En un bucle usalmente hay una variable que cambia de valor hasta que llega un momento que la condición es falsa y el bucle para"
    h "Sino la condicion inicial no se torna {color=#f00}falsa{/color} cuando tenemos un bloque {color=#ff0}while{/color}, tenemos un {color=#ff0}bucle infinito{/color},\nes decir un bloque que se repetirá hasta que el programa se cierre forzosamente o se apague el computador"
    h "Aunque en ocasiones se requiere un bucle infinito, en general debe evitarse"
    consola "{color=#f0f}#Veamos un ejemplo de un bucle {color=#ff0}while{/color}{/color}\ni=0\nwhile i<4:\n\ \ \ \ print(i)\n\ \ \ \ i +=1\n1\n2\n3"
    consola "{color=#f0f}#Veamos un ejemplo de un bucle {color=#ff0}infinito while{/color}{/color}\ni=0\nwhile True:\n\ \ \ \ print(i)\n\ \ \ \ i +=1\n1\n2\n3\n...{color=#f0f}#Se repite para siempre :("
    consola "{color=#f0f}#Veamos otro un bucle {color=#ff0}infinito while{/color}{/color}\ni=0\nwhile i > -5:\n\ \ \ \ print(i)\n\ \ \ \ i +=1\n1\n2\n3\n...{color=#f0f}#También se repite para siempre :("
    h "Además del control de flujo con {color=#ff0}else{/color} que significa {color=#ff0}sino{/color} y debe estar precedido por una linea/bloque {color=#ff0}if{/color} o {color=#ff0}while{/color}"
    h "La línea o bloque {color=#ff0}else{/color} se corre una vez cuando la condición evaluada en la sentencia {color=#ff0}if{/color} o {color=#ff0}while{/color} se torna falsa"
    consola "{color=#f0f}#Veamos un ejemplo de un ejemplo {color=#ff0}if es cierto {/color}{/color}\na=2\nif a:\n\ \ \ \ x=3\nelse:\n\ \ \ \ x=2\nx\n3"
    consola "{color=#f0f}#Veamos un ejemplo de un ejemplo {color=#ff0}if es falso {/color}{/color}\na=2\nif a > 2:\n\ \ \ \ x=3\nelse:\n\ \ \ \ x=2\nx\n2"
    consola '{color=#f0f}#Veamos un ejemplo de un ejemplo con {color=#ff0}while{/color} en Python 2{/color}\na=3\nwhile a > 0:\n\ \ \ \ a -= 1\n\ \ \ \ print a\nelse:\n\ \ \ \ print "Boom!"\n2\n1\n0\n"Boom!"'
    h "Finalmente tenemos la palabra reservada {color=#ff0}elif{/color} la cual {color=#f00}no existe en inglés{/color}, es una contracción de else e if"
    h "Funciona igual que una sentencia {color=#ff0}if{/color} y puede estar precedida de otra sentencia {color=ff0}if{/color} con su respectiva línea o bloque"
    h "Tambien puede estar precedida de una o más sentencias {color=#ff0}elif{/color} siempre y cuando el segundo bloque {color=#ff0}elif{/color} sea precedido por un bloque {color=#ff0}if{/color}"
    consola "{color=#f0f}#Veamos un ejemplo de un ejemplo {color=#ff0}if es falso {/color}, pero condición del {color=#ff0}elif{/color} es cierta{/color}\na=2\nif a > 2:\n\ \ \ \ x=3\nelif a==2:\n\ \ \ \ x=0\nelse:\n\ \ \ \ x=1\nx\n0"
    consola "{color=#f0f}#Veamos un ejemplo de un ejemplo {color=#ff0}if es falso {/color}, pero condición del {color=#ff0}elif{/color} es falsa{/color}\na=1\nif a > 2:\n\ \ \ \ x=3\nelif a==2:\n\ \ \ \ x=0\nelse:\n\ \ \ \ x=1\nx\n1"
    #Calendario chino
    h "Vamos a hacer algo divertido con lo aprendido hasta ahora"
    h "Voy a crear una lista de objetos (todos tipo int) llama {color=#ff0}lista_Anos{/color} en Ren'py"
    $ lista_Anos = [1978,1985,1966]
    h "La acabo de crear"
    h "El valor de la variable {color=#ff0}lista_Anos{/color} se ha cargado a Ren'py y su valor es [lista_Anos]"
    $ bad_data=False
label q23:
    $ lista_Anos = [1978,1985,1966]
    if bad_data:
        h "Ingresa los datos correctamente"
        h "¿Cómo yo se que los datos son inválidos?"
        h 'Es algo que vamos a ver más adelante llamado "Expresiones regulares"'
        h "Las expresiones regular me permiten analizar el texto que estás introduciendo al programa"
        h "Ellas te permiten tomar acciones (mediante bloques {color=#ff0}if{/color}, {color=#ff0}else{/color} y {color=#ff0}elif{/color}) dependiendo del valor de una variable cadena"
        h "Como es este caso particular"
        h "Te recomiendo leer acerca de las expresiones regulares en la {a=https://es.wikipedia.org/wiki/Expresi\%C3\%B3n_regular}wikipedia{/a}"
        h "Cada vez que te equivoques regresarás a ver estos diálogos nuevamente\n:)"
    python:
        import re
        nac = renpy.input("¿Cuál es tu fecha de nacimiento? -Ingresa las 4 del año de tu nacimiento\nIngresa un dato incorrecto y aprenderás algo nuevo")
        nac=nac.strip()
        
        if re.search("((19[5-9]|20[01])\d)",nac):
            nac = int(nac)
            if not nac in lista_Anos:
                lista_Anos.append(nac)
        else:
            bad_data=True
            renpy.jump('q23')
    h "Has ingresado el año [nac]"
    if len(lista_Anos) == 3:
        h "Ese año está en la lista original, por lo que no lo voy a repetir"
        h "¿Cómo sé eso?\nPorque antes de intentar añadirlo a la lista, usé el siguiente bloque:\nif not nac in lista_Anos:\n\ \ \ \ lista_Anos.append(nac)"
        h "En este caso, {color=#ff0}nac in lista_Anos{/color} es cierto, pero como está precedido por el operador {color=#ff0}not{/color} se lo convierte en falso"
        h "Por lo que no se agrega a la variable que contiene la lista {color=#ff0}lista_Anos{/color}"
        h "Todos estos diálogos están dentro de un bloque {color=#ff0}if{/color} que se ejecuta si el número de elementos de la lista es 3 (es decir que no lo añadí a la variable)"
    else:
        h "Ese año no está en la lista original, por lo que lo voy a añadir a la lista"
        h "¿Cómo sé eso?\nPorque antes de intentar añadirlo a la lista, usé el siguiente bloque:\nif not nac in lista_Anos:\n\ \ \ \ lista_Anos.append(nac)"
        h "En este caso, {color=#ff0}nac in lista_Anos{/color} es falso, pero como está precedido por el operador {color=#ff0}not{/color} se convierte en cierto"
        h "es decir que el bloque {color=#ff0}lista_Anos.append(nac){/color} se ejecuta"
        h "por lo que he agregado el número [nac] a la variable que contiene la lista {color=#ff0}lista_Anos{/color} que ahora es [lista_Anos]"
        h "Todos estos diálogos están dentro de un bloque {color=#ff0}else{/color}"
        h "Este bloque else, es precedido por un bloque if que es cierto si el número de elementos dentro la lista es 3"
        h "Como el añadimos una elemento a la variable, la condición se torna falsa y se ejecuta este bloque de diálogos else"
    h "Ahora voy a hablar de los signos zodicales chinos y a cual signo corresponde [nac]"
    h "Existen varias formas de saber que signo zodiacal chino es [nac]"
    h "El calendario chino asigna un animal a cada año y son 12 animales"
    
    $ signos_Chinos= ["mono", "gallo", "perro", "cerdo","rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "cabra" ]
    h "Si el año es divisible entre doce es el año del mono, pero si al año le restamos 1 y luego se vuelve divible entre 12 tenemos el año del [signos_Chinos[1]]"
    h "Si el año le restamos 2 y se vuelve divisible entre 12 es el año del [signos_Chinos[2]]"
    $ error=""
label qChino1:
    if error:
        h "[error]"
    menu:
        '¿Qué operador aritmético en Python nos permite calcular lo que "sobra" después de una división?'
        "+":
            jump qChino1
            $ error="Eso no es correcto, el operador de la suma no permite calcular eso"
        "-":
            jump qChino1
            $ error="Eso no es correcto, el operador de la resta permite calcular eso, pero es muy complicado"
        "*":
            jump qChino1
            $ error="Eso no es correcto, el operador de la multiplicación no permite calcular eso"
        "\%":
            $ error=False
            jump q24
        "**":
            jump qChino1
            $ error="Eso no es correcto, el operador de la exponenciación no tiene vela en este entierro"
        "/":
            jump qChino1
            $ error="Eso no es correcto, el operador de la división permite calcular eso, pero es muy complicado"
label q24:
    $ signos_Chinos= ["mono", "gallo", "perro", "cerdo","rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "cabra" ]
    hide text
    $ nac=1923
    h "En efecto, podemos simplemente calcular el residuo mediante el operador del mismo es decir {color=#ff0}\%{/color}"
    h "Una división entre 12 que no deja residuo de 0, habla de un número divisible entre 12. Lo que corresponde al año del mono. Si el residuo es de 1, es del gallo, etc"
    show text "{size=40}{color=#000}0-[signos_Chinos[0]]   1-[signos_Chinos[1]]    2-[signos_Chinos[2]]\n3-[signos_Chinos[3]]    4-[signos_Chinos[4]]    5-[signos_Chinos[5]]\n6-[signos_Chinos[6]]   7-[signos_Chinos[7]]   8-[signos_Chinos[8]]\n9-[signos_Chinos[9]]   10-[signos_Chinos[10]]   11-[signos_Chinos[11]]{/color}{/size}"  at truecenter 
    h 'Arriba vemos una lista de los residuos de cada año y abajo la lista creada:\n{color=#ff0}signos_Chinos = [["mono", "gallo", "perro", "cerdo","rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "cabra" ]{/color}'
    $ mod= int(nac % 12)
    h "El residuo de dividir [nac] entre 12 es [mod]"
    $ yr= signos_Chinos[mod]
    python:
        if mod in  [4,9,11]:
            articulo= "de la"
        else:
            articulo= "del"
    h "El residuo de dividir [nac] entre 12 es [mod] \nEs decir que el año [nac] corresponde año [articulo] [yr]"
    h "La otra alternativa es usar el control de flujo"
    $ del signos_Chinos
    hide text
    h "acabo de eliminar la lista de signos_Chinos"
    h "Podemos usar una serie de if, else y elif y crear una variable llamada tipo cadena signo que var"
    python:
        if not mod:
            signo="mono"
        elif mod == 1:
            signo="gallo"
        elif mod == 2:
            signo="perro"
        elif mod == 3:
            signo="cerdo"
        elif mod == 4:
            signo="rata"
        elif mod == 5:
            signo="buey"
        elif mod == 6:
            signo="tigre"
        elif mod == 7:
            signo="conejo"
        elif mod == 8:
            signo="dragón"
        elif mod == 9:
            signo="serpiente"
        elif mod == 10:
            signo="caballo"
        else:
            signo="cabra"
    consola 'if not mod:\n\ \ \ \nsigno="mono"\nelif mod == 1:\n\ \ \ \nsigno="gallo"\nelif mod == 2:\n...\nelif mod == 10:\n\ \ \ \nsigno="caballo"\nelse:\n\ \ \ \nsigno="cabra"'
    h "Al ejecutar el control de flujo tenemos que signo tiene el valor de [signo]"
label funciones:
    show text "{size=40}{color=#000}Capítulo seis\n\n\nLas funciones{/color}{/size}" at top
    h "Ahora vamos a hablar de las funciones"
    h "Las funciones no son más que bloques de códigos que se pueden ejecutar en una sentencia"
    h "Las funciones pueden ser {color=#ff0}predeterminadas{/color}, {color=#ff0}asociadas a un módulo{/color}, ser un {color=#ff0}método{/color} o ser {color=#ff0}definidas por el desarrollador{/color}"
    h "Hemos visto funciones como int(), bool(), str(), print(), len() entre otras son funciones {color=#ff0}predeterminadas{/color}, simplemente ponemos sus {color=#ff0}argumentos{/color}"
    h "Las funciones asociados a un módulo requieren que {color=#ff0}importe{/color} 
       el módulo, y luego se debe escribir el nombre del módulo seguido por un punto {color=#ff0}(.){/color}, luego el nombre de la función seguida por paréntesis con los argumentos adentro"
    consola "{color=#f0f}#Por ejemplo, para sacar la raíz cuadrada de un número usando el módulo math{/color}\nimport math\nmath.sqrt(144)\n12"
    consola "{color=#f0f}#tambien podemos seleccionar una función del módulo usando from e import: sin necesidad de usar la notación con punto{/color}\nfrom math import sqrt\nsqrt(196)\n14"
    h "Voy a hablar de los {color=#ff0}métodos{/color} debo hablar de las funciones definidas por el desarrollador"
    h "Como había dicho anteriormente, las funciones definen un bloque de código python mediante una sola sentencia"
    h "Vamos a crear una función que multiplique 2 números"
    h "Hay dos palabras reservadas: lambda y def"
    consola "{color=#f0f}#Eso ya lo habíamos visto{/color}\nimport math\nmath.sqrt(144)\n12"
    h "Vamos a usar la palabra {color=#ff0}def{/color} para crear un archivo tipo {color=#ff0000}script{/color} llamado {color=#ff0}semaforo.py{/color}"
    h "Vamos a crear un archivo de texto plano llamado semaforo.py, con el editor de texto..."
    h "En Windows notepad, en Mac no se, en Android es el File Editor, o podemos usar cualquier otro.\nAl instalar Python in Windows, éste trae su propio editor, pero eso es irrelevante!, lo importante es escribir..."
    h "escribimos las siguientes líneas, los comentarios pueden escribirse o ser ignorados"
    consola "# -*- coding: utf-8 -*-\n#El comentario de arriba es necesario para usar tildes y la ñ\n#Esta línea importa la función randint del módulo random\nfrom random import randint\n#Luego creamos una función llamada semáforo\ndef semaforo():\n\ \ \ \ x=randint(0,1)\n\ \ \ \ if x:\n\ \ \ \ \ \ \ \ print \"El carro avanza\"\n\ \ \ \ else:\n\ \ \ \ \ \ \ \ print \"El carro se detiene\"\nsemaforo()"
    h "En Mac y en Linux podemos abrir la línea de comandos y escribir\npython semaforo.py\ny veremos el resultado..."
    h "En Windows es un más complicado..."
    h "En Windows, después de bajar Python e instalarlo, tendrán accesso al IDLE"
    h 'Necesitan abrir el IDLE y buscar en el menú "archivo", y buscar el archivo semaforo.py'
    h "Se les mostrará el código fuente y con presionar F5, se ejecutará"
    h "Vamos a modificar un poquito para mostrarle como usar los argumentos"
    h "Vamos a llamar este nuevo archivo semaforo2.py"
    consola "# -*- coding: utf-8 -*-\n#El comentario de arriba es necesario para usar tildes y la ñ\n#Esta línea importa la función randint del módulo random\nfrom random import randint\n#Luego creamos una función llamada semáforo\nx=randint(0,1)\ndef semaforo(x):\n\ \ \ \ if x:\n\ \ \ \ \ \ \ \ print \"El carro avanza\"\n\ \ \ \ else:\n\ \ \ \ \ \ \ \ print \"El carro se detiene\"\nsemaforo()"
    h 'Si corremos semaforo2.py tendremos un error, debido a problemas con el {color=#ff0}ámbito{/color} llamado en inglés "{color=#ff0}scope{/color}".'
    h "Dentro de una función, los argumentos y cada una de las variables tienen un {color=#ff0}ámbito local{/color}\nestas variables solamente existen DENTRO de la función"
    h "Fuera de este ámbito local, ¡ninguno de estos elementos existen!"
    h "Del mismo modo, el los elementos de un bloque if NO existen si la condición no se lleva a cabo"
    h "Vamos a ver si comprendiste estos conceptos"
    hide text
    
label funq1:
    pass
    
    return
return