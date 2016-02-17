
image python_logo ="images/Python logo.png"
image reloj=im.FactorScale("images/reloj.png", 0.25)
image reloj guts=im.FactorScale("images/reloj engranajes.jpg", 0.25)
image white ="#ffffff"
define h = Character('Hedley', color="#c8ffc8")
$tipJar="https://www.paypal.me/HedleyQuintana"

# The game starts here.
# - El juego comienza aquí.
label start:
    scene white with dissolve
    show python_logo at truecenter
    h "Saludos a todos, me llamo Hedley!"
    h "Les voy a enseñar a programar en Python"
    h "Y para sonar más interesante, les digo..."
    h "que este tutorial, está desarrollado en Ren'py"
    h "el cual es una implentación de Python"
    h "vamos a empezar..."
    jump chp1
label chp1:
    show text "{size=40}{color=#000}Capítulo uno\n\n\n¿Qué es programar?{/color}{/size}" at top
    h "Empezamos..."
    h "Para mi, aprender a programar me pareció bastante frustrante!"
    h "Verán aprendí varios lenguajes de programación, pero no supe lo que era programar..."
    h "Vamos a intentar aprender a programar antes de entrar de lleno a Python"
    h "Vamos a iniciar con el concepto del {color=#ff0}proyecto{/color}"
    h "Los {color=#ff0}proyectos{/color} están asociados a 2 conceptos:"
    h 'El primero es que el proyecto debe tener la finalidad de {color=#ff0}resolver un problema{/color}'
    h 'El {color=#ff0}problema{/color} es de caracter repetitivo y se resuelve mediante la {color=#ff0}interacción{/color} de partes de un {color=#ff0}sistema{/color}'
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
    label q2:
        show python_logo at truecenter
        h "La nube es la opción incorrecta! vamos adelante"
        h "Vamos a ver un ejemplo tangibles"
        h "veamos un reloj..."
        hide python_logo
        show reloj at truecenter
        h "el reloj analógico es un {color=#ff0}sistema complejo{/color} que permite saber la hora"
        h "mediante el movimiento de sus 3 manecillas a diferentes velocidades"
        hide reloj
        show reloj guts at truecenter
        h "para serles sinceros no se como trabajan los relojes, pero lo que sí se"
        h "es que los engranajes (o ruedas dentadas) trabajan de manera coordinada a {color=ff0}diferentes velocidades{/color} para posicionarse"
        h "y contestar a la pregunta {color=#ff0}\"¿Qué hora es?\"{/color}"
        h "Las manecillas se mueven de forma implacable con el pasar de tiempo..."
        
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
            python:
                del error
                del count
            jump n2
label n2:
    show python_logo at truecenter
    if error == "":
        h "Veo que no cometido errores!"
        h "Has acertado a la primera..."
        $peerless=True
    else:
        $peerless=False
        h "Has seleccionado [count] veces la opción incorrecta"
        h "Cometer errores, es muy importante para aprender cualquier lenguaje de programación..."
    $del peerless
    
    show python_logo at truecenter
    h "Veo que han notado que a diferencia de los otros objetos o sistemas, los {color=#ff0}clavos son bastante simples{/color}."
    h "Ellos no tienen otras partes dentro y pueden servir para crear objetos más grandes y complejos"
    if peerless:
        h "Vamos a recapitular, el carro tiene muchas piezas, las cuales hacen muchas funciones!"
        h "El cuerpo humano tiene muchas órganos y células organizadas que permite que estemos vivos"
        h "La página web muchos elementos: interaccionan con el usuarios, tienen una serie de piezas más simples otras páginas, manejan bases de datos"
        h "Los juegos de video son sistemas muy complejos que interaccionan con el usuarios: tienen piezas más simples que manejan a enemigos, al puntaje, en fin todo un enredo"
    h "El ejercicio de imaginarse como podemos \"desmembrar\" un sistema complejo en sus componentes fundamentales y sus relaciones es el primer paso para poder programar"
    h "A esto se le llama {color=#ff0}abstracción{/color}"
    
    h "En Python, tenemos algo equivalente a los clavos o unidades fundamentales"
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    h "La abstracción es tratar de sacar cada una de las piezas que forman un sistema"
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
    h "Ya que hablamos del sistema digestivo... vamos a hacer algo"
    python:
        digestivo=["boca","faringe","esófago", "estómago", "intestino delgado", "intestino grueso", "ano"]
        check_organ=""
        digestivo_counter=9
        cont="No puede proseguir hasta que complete la tarea"
    hide text
    hide python_logo
    jump q6
label q6:
    if digestivo_counter == 9:
        python:
            cabecera= "Señale el órgano del tubo digestivo que se encuentra en la cabeza"
            digestivo_counter = 0
    else:
        if digestivo_counter < 6:
            if check_organ == digestivo[digestivo_counter]:
                python:
                    digestivo_counter += 1
                    organo = check_organ
                if digestivo_counter < 2:
                    $cabecera = "Qué órgano sigue a la "+ organo
                else:
                    $cabecera="Qué órgano sigue al " + organo
            else:
                if digestivo_counter > 0:
                    h "{color=#f00}Ese órgano no es el que sigue!{/color}"
                else:
                    h "{color=#f00}Ese órgano no está en la cabeza!{/color}"
            
    
        elif digestivo_counter == 6:
            h "Y así tenemos que el último órgano es el ano"
            $cont="Haga click aquí para continuar"
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
        "[cont]":
            if cont == "No puede proseguir hasta que complete la tarea":
                jump q6
            else:
                jump n4
label n4:
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    h "Wao, hemos visto como se conectan los órganos del tubo digestivo uno tras otro"
    h "En el caso del carro, del reloj, la página web y del video juego podemos hacer exactamente lo mismo..."
    h "Aún más NO necesitamos ningún programa para ver como estos elementos se relacionan entre sí"
    h "Podemos agarrar un pedazo papel y describir los elementos, su comportamiento, como se relacionan unos con los otros "
    h "Este {color=#ff0}diseño{/color} es fundamental para saber las acciones y definir nuestro programa"
    h "Creo que estamos listos para ver como representamos esos sistemas y elementos en nuestro programa"
    h "Antes de hablar de como hacer esas {color=#ff0}abstracciones{/color} en Python tengo que mostrarles las {color=#ff0}variables{/color}, los {color=#ff0}operadores{/color} y las {color=#ff0}funciones{/color}"
    hide text
    show text "{size=40}{color=#000}Capítulo tres\n\n\nLas variables{/color}{/size}" at top
    h "Antes de examinar el concepto de las variables en Python, vamos a instalarlo"
    h "Python es un idioma multiplataforma"
    h "Es decir como casi todos los lenguajes de programación, este crea programas el cual va a correr independientemente del sistema operativo"
    h "Si estás corriendo este tutorial desde una computadora u ordernador que corre Mac OS o Windows, debes ir a la página web de Python donde puedes bajar el instalador para la plataforma {a}www.python.org{/a}"
    h "Si estás corriendo esto en Android hay 2 maneras de correr Python"
    h "la forma \"difícil\" que es instalando una aplicación de terminal e instalando Python desde allí (por cierto este método ocupa mucho espacio en el celular)"
    h "O bajando el app \"QPython\", el cual le va a dar los elementos necesarios para correr python en su teléfono inteligente o tableta"
    h "Una vez que hayas hecho eso, podemos seguir..."
    h "Las variables son un objecto que contiene cierta información que se va a reutilizar más tarde"
    h "En alguno de los ejercicios anteriores, he usado variables, por ejemplo... te acuerdas cuando conté el número de errores los ejercicios anteriores? esa información la guardé en una variable"
    h "Para crear una variable, debemos tener 3 elementos: el {color=#f00}nombre de la variable{/color}, el {color=#f00}operador de asignación{/color} y su {color=#f00}valor{/color}."
    h "es decir por ejemplo a = 16.29"
    h "Es importante destacar que hay ciertas reglas para nombrar una variable"
    h "Las variables puedes nombrarla \"como quieras\" (lo pongo entre comillas por algo), pero su nombre solo puede contener signos de subrayado(_), letras y números."
    h "Las variables tampoco pueden ser \"palabras reservadas\" del lenguaje Python, las cual aprenderemos más adelante, dichas palabras son de uso común en inglés, pero no en español"
    h "Y el nombre nunca puede iniciar con un número"
    h "Para reutilizar la variable debemos escribir respetando las mayúsculas y minúsculas: la variable A no es lo mismo que la variable a"
    h "Ok, vamos a repasar lo aprendido"
    hide text
label q7:
    if error!="":
        h "Epa! El nombre [error] es perfectamente legal"
    if error=="_import":
        h "import es un nombre ILEGAL en Python y no lo puedes usar"
        h "Más adelante verás por qué..."
        h "Sin embargo, tanto _import como import_ son nombres permitidos"
    menu:
        "Cual de los siguientes nombres no es ilegal en Python"
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
        "¿Qué problemas tiene ese nombre?":
            $error ="Ponga atención a las otras opciones"
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
    h "Las variables Astoide4 y la variable _import tienen algun sentido..."
    h "La idea de Python es de servir como un lenguaje de \"alto nivel\", es decir ser \"entendible\" para los humanos"
    h "Aunque no tanto para el ordenador o computadora"
    h "Variables con un nombre como \"_asTAS45\" hacen que todo se enrede a menos que tenga una lógica interna"
    hide text
    
label q9:
    menu:
        "Python es un lenguaje de programación de alto nivel, ¿qué significa esto?"
        "Que Python es mucho más comprensible para los desarrolladores que para las máquinas donde se corre":
            h "CORRECTO"
            jump n7
        "Que Python es mucho más comprensible para las máquinas donde se corre que para los desarrolladores de programas":
            h "¡Eso no es correcto!"
            jump q9
        "Que es un lenguaje de alto nivel de complejidad":
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
        "[encabezado]"
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
    h "{color=#f0f}#Por ejemplo{/color}\n{color=#ff0}peso_Mujer=70.0\ntype(peso_Mujer)\n\<type 'float'\>{/color}"
    h "{color=#f0f}#O también, puedes omitir los ceros{/color}\n{color=#ff0}peso_Mujer=70. {color=#f0f}#Nota que no hay ceros{/color}\ntype(peso_Mujer)\n\<type 'float'\>{/color}"
    h "Python deduce el tipo de variable como cadena ({color=#ff0}str{/color}), si escribimos cualquier cosa entre un par de comillas dobles \"\" o simples ''"
    h "{color=#f0f}#Por ejemplo{/color}\n{color=#ff0}peso_infante='20.0 kilogramos'\ntype(peso_infante)\n\<type 'str'\>{/color}"
    h "Y finalmente las variables booleanas, son la que solo pueden tener 2 valores cierto o {color=#ff0}True{/color} y falso {color=#ff0}False{/color}"
    h "Vamos al siguiente ejercicio"
    hide text
    $digestivo_counter=0
    $check=""
label q11:
    $tipos=["str", "float", "int", "float","bool"]
    $valores=['"Rosa"', "60.5", "123", "24.", "False"]
    
    if check=="":
        pass
    elif check == tipos[digestivo_counter]:
        h "CORRECTO"
        $digestivo_counter += 1
        if digestivo_counter == 5:
            h "Has determinado los tipos de las variables, vamos a proseguir hablando de los operadores aritméticos y lógicos"
            jump n9
    else:
        h "¡Eso no es correcto!"
    $encabezado="Determine el tipo Python de la variable cuyo valor es: " + valores[digestivo_counter]
    menu:
        "[encabezado]"
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
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos, de asignación y lógicos{/color}{/size}" at top
    h "Los operadores nos permiten crear nuevas variables o resultados a partir de 2 o más variables o valores"
    h "Los primeros operadores que vamos a ver son los {color=#ff0}operadores aritméticos{/color}, los cuales crean nuevos números a partir de otros números"
    h "Los operadores aritméticos que vamos a ver son el de la suma {color=#ff0}+{/color}, la resta {color=#ff0}-{/color}, la multiplicación {color=#ff0}*{/color}, la división {color=#ff0}/{/color}, el residuo {color=#ff0}\%{/color} y la exponenciación {color=#ff0}**{/color}"
    h "La suma y la resta son bastante sencillas, veamos unos ejemplos"
    h "1+1\n2"
    h "3-2\n1"
    h "24-45\n-21"
    h "Claro está... debemos recordar que hay dos tipos de varibles numéricas, las de tipo entera ({color=#ff0}int{/color}) y las de tipo flotante que manejan decimales ({color=#ff0}float{/color})"
    h "La suma o resta de dos o más variables de tipo entera producen un entero, y si hay por lo menos una variablo de tipo flotante, se produce un resultado flotante"
    h "{color=#ff0}#Es decir{/color}\n1+1\n2\n1.2+1\n2.2\n2.3-1-3\n1.7"
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
    show text "{size=40}{color=#000}Capítulo cuatro\n\n\nLos operadores aritméticos, de asignación y lógicos{/color}{/size}" at top
    h "La multiplicacion, la división y el residuo son un poquito especiales"
    h "Igual que lo que ocurre con la suma y la resta, estás operaciones entre enteros resultan en un entero y si hay por lo menos un flotante involucrado, tendremos un flotante"
    h "En el caso de la multiplicación, eso no es mucho problema"
    h "{color=#f0f}Multiplicacion de enteros{/color}\n3*5\n15"
    h "{color=#f0f}Multiplicacion con flotantes{/color}\n3.0*5.*8.0\n90.0"
    h "{color=#f0f}Multiplicacion con por lo menos un enteros{/color}\n3.0*5*8\n90.0"
    h "En el caso de la división es un poco especial, debido que al dividir, no vamos a obtener necesariamente un número entero"
    h "Si dividimos dos enteros vamos a obtener la {color=#ff0}parte entera de la division{/color}"
    h "{color=#f0f}Sabemos que 48 entre 8 es 6{/color}\n48/8\n6"
    h "{color=#f0f}Pero 50 entre 8 tambien es 6{/color}\n50/8\n6"
    h "{color=#f0f}Aun más 55 entre 8 tambien es 6{/color}\n55/8\n6"
    h "{color=#f0f}Claro está 56 entre 8 es 7{/color}\n56/8\n7"
    h "Las operaciones con flotantes, se toman en cuenta los decimales por lo que.."
    h "{color=#f0f}Aun más 55 entre 8 es 6.87{/color}\n55.0/8\n6.87"
    h 'El residuo es lo "sobra" despues de dividir con enteros'
    h 'Es decir, 55 entre 8 es 6, pero como 6*8 es 48, el "residuo" sería 7 es decir 55-48 es 7'
    h "55\%8\n7"
    h "23\%5\n3"
    h "El residuo es importante para valorar los números pares de los impares"
    h "Los números pares al dividirse entre 2 tienen un residuo de 0, pero los impares tienen un residuo de 1"
    hide text
    $error=""
label q13:
        if error:
            h "[error]"
        menu:
            "¿Cuanto es el valor de 135\%2?"
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
    h "#En el caso de la suma:\n2+3\n5\n#Y su operación opuesta es la resta\n5-3\n2"
    h "#En el caso de la multiplicación:\n5*6\n30\n#Y su operación opuesta es la división\n30/5\n6"
    h "En la exponenciación tenemos 2 operaciones opuestas: la \"radicación\" y el \"logaritmo\""
    #Figura de la radicación
    h "En el caso de la radicación tenemos 2 componentes, que son el radical y el índice"
    h "El objetivo de la radicación es obtener el número que al multiplicarse por si mismo las veces dadas por el índice da por resultado el radical"
    h "Los índides siguen las mismos nombres (en matemáticas) de los exponentes de la exponenciación: raíz cuadrada (2), raíz cúbica (3), raíz cuarta (4), etc "
    h "Por ejemplo, la raíz cuarta de 1296 es 6, porque 6*6*6*6 es 1296 o bien 6**4 es 1296"
label q14:
    
    h "**Python no tiene ninguna función (de manera predefinida) para calcular raíces"
    h "Sin embargo, es posible calcular cualquier raíz de cualquier índice usando uno de los 2 métodos"
    h "Un método es primero importar un módulo llamado math y luego usar un método llamado sqrt"
    h "Si usamos este método SOLAMENTE podemos calcular raíces con indices pares..."
    h "Vamos a calcular la raíz cuadrada de 25 (que sabemos que es cinco)"
    h "Lo primero es importar el módulo de mas matemáticas"
    h "Lo hacemos con la palabra reservada {color=#ff0}import{/import}"
    h "#Es decir\nimport math"
    h "Y luego usamos el metodo sqrt de math asi"
    h "#Raiz cuadrada de 25\nimport math\nmath.sqrt(25)\n5.0"
    h "También podemos dar un alias más amigable al módulo usando la palabra reservada {color=#ff0}as{/color} que en inglés significa {color=#ff0}como{/color}"
    h "#Raiz cuadrada de 25\nimport math as m\nm.sqrt(25)\n5.0"
    h "También podemos dar importar la funcion sqrt del módulo math usando las palabras reservadas {color=#ff0}from{/color} que en inglés significa {color=#ff0}desde{/color}"
    h "#Raiz cuadrada de 25\nfrom math import sqrt\nsqrt(25)\n5.0"
    h "Tambien podemos usar ambas palabras reservadas"
    h "#Raiz cuadrada de 25\nfrom math import sqrt as raizCuadrada\nraizCuadrada(25)\n5.0"
    h "Podemos calcularlo de otra manera, teniendo en cuenta que la raíz cuadrada de un número es lo mismo que elevarlo a la 1/2\nla raíz cúbica es lo mismo que elevarlo a la 1/3, la cuarta a la 1/4, etc"
    h "Sin necesidad de importar ningún módulo podemos calcular la raíz cuadrada de 25 así"
    h "#Raiz cuadrada de 25\nhalf=1.0/2.0\n25**half\n5.0"
    h "El objetivo del logaritmo es el cálculo del exponente si sabemos la base y la potencia"
    h "Si sabemos de 4*4, o 4**2 es 16, entonces el logaritmo de 16 con base 4 es 2"
    h "En Python, para calcular el logaritmo debemos importar el método log del módulo math para calcular el logaritmo"
    h "#Para calcular el logaritmo de 16 con base 2\nimport math\nmath.log(16,2)\n4.0"
    $error=""
    $digestivo_counter=0
    $respuesta=10
label q15:
    $ encabezado="Calcule usando Python:\n"
    $ encabezados = ["Siete elevado a la quinta potencia", "La raíz cuadrada de 64 usando el módulo math", "La raíz cuadrada de 49 usando un flotante como exponente"]
    $ Menus = [ ["7*5", "7**5", "7***5"],
                ["import math\nmath(64,2)", "import math\nsqrt(64)", "from math import sqrt as Rcuadrada\nRcuadrada(64)"],
                ["49**0.5", "0.5**49", "float(49)**2"]]
    $ claves =[1,2,0]
    
    if respuesta==10:
        pass
    elif respuesta == claves[digestivo_counter] and digestivo_counter < 3:
        $digestivo_counter += 1
    else:
        $error="¡Eso no es correcto!"
    if error:
        h "[error]"
        $error=""
    if digestivo_counter <=3:
        if digestivo_counter < 3:
            h "CORRECTO"
            h "Vamos por el siguiente reto"
        else:
            h "Exacto, has concluido este ejercicio"
            jump n12
    $encabezado += encabezados [digestivo_counter]
    $Menu1=Menus[digestivo_counter][0]
    $Menu2=Menus[digestivo_counter][1]
    $Menu3=Menus[digestivo_counter][2]
    menu:
        "[encabezado]"
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
    $error=""
label q16:
    h "Vamos a ver un {color=#ff0}lienzo{/color}, en inglés llamado {color=#ff0}canvas{/color}"
    h "En la implementación Python 'Pygame' y en las páginas web, el lienzo (o canvas) representa un sistema de coordenadas con el origen en la esquina superior izquierda"
    menu:
        "Si tenemos una variable x que contiene la distancia de un objeto O en milimetros desde el borde izquierdo del lienzo\ny una variable y que contiene la distancia en milimetros desde el borde superior del lienzo\n¿Cual de estos códigos Python representa la variable d que contrine la distancia entre el objeto y la esquina superior izquierda?"
        "d=(y**2+x**2)**.5":
            h "¡Correcto!"
        "d=(x**2+y**2)**5":
            h "¡Eso no es correcto!"
            jump q16
        "d=(x**2+y**2)**.5+O":
            h "¡Eso no es correcto!"
            jump q16
label n13:
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
    h "x=5\nx += 2\nx\n7\nx += 2\nx\n9"
    h "En operador de decremento aditivo, {color=#ff0}-={/color}, es similar al de incremento, pero en lugar de subir el valor de la variable, lo baja"
    h "vidas=3\nvidas -= 1\nvidas\n2\nvidas -= 1\nvidas\n1"
    h "En operador de incremento multiplicativo, {color=#ff0}*={/color}, es similar al de incremento aditivo, pero en lugar de sumar el valor de la variable, lo sube multiplicando por el valor de la derecha"
    h "vidas=5\nvidas *= 2\nvidas\n10\nvidas *= 4\nvidas\n40"
    h "En operador de decremento multiplicativo, {color=#ff0}/={/color}, es similar al de incremento multiplicativo, pero en lugar de multiplicar el valor de la variable, lo disminuye dividiendo por el valor de la derecha"
    h "municiones=42\nmuniciones /= 5\nmuniciones\n8\nmuniciones /= 2\nmuniciones\n4"
    h "Vamos a ver el siguiente ejercicio"
    $error=""
label q17:
    if error:
        h "[error]"
        $error=""
    menu:
        "Calcule el valor de la raciones despues de ejecutar el codigo\nraciones=25\nraciones -= 7\nraciones"
        "Error de compilacion":
            $ error= "No veo ningun error en ese código"
            jump q17
        "3":
            h "Correcto, al dividir entre 2 enteros, obtenemos otro entero, es decir 25/7=3"
        "3.5714285714285716":
            $error="¡Qué número más enredado!, esa no es la respuesta correcta"
            jump q17
label n14:
    h "Antes de terminar con estos dichosos operadores aritméticos, voy a habar de la {color=ff0}coerción{/color} de variables"
    h "Había dicho anteriormente que el resultado de uno o más operadores aritméticos es un número entero o flotante"
    h "También había dicho que existen 2 tipos variable numéricas en Python (int y el float) y otros 2 tipos que son la cadena (string) y el boolean"
    h "Si aplicamos cualquiera de estos operadores entre un número y una cadena (string) vamos a tener un error de compilación (así de simple)"
    h "Si tenemos operaciones aritméticas entre un enteros y por lo menos un boolean, el boolean se convierte o {color=#ff0}coerciona{/color} a un entero de valor 1 si es True y 0 si es False"
    h "Si tenemos operaciones aritméticas con por lo menos un número flotante y por lo menos un boolean, el boolean se {color=#ff0}coerciona{/color} a un flotante de valor 1.0 si es True y 0.0 si es False"
    h "#Por ejemplo\n2+2+True+False\n5"
    h "#Otro ejemplo\n2+2+True+False*3.+234**False\n6.0"
    h "Vamos a ver otro ejercicio"
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
    h "Al fin acabamos con esos operadores aritméticos y de asignación"
    h "Vamos a ver 2 operadores que solo sirven para cadenas (strings) que el operador de concatenación y de formato"
    h "El operador de concatenación es {color=#ff0}+{/color}, el cual es idéntico al de la suma, pero cuando está entre strings va a concatenarlos, es decir va a unir dos o más cadenas hacer una cadena más largo"
    h '"Hola "+ "mundo!"\n"Hola mundo"'
    h '"Hola, "+"¿cómo "+ "estás?"\n"Hola, ¿cómo estás?"'
    h 'saludo="Hola, "\nnombre="Pepe"\nsaludo+nombre\n"Hola, Pepe"'
    h 'El otro operador es la "interpolación" de variables'
    h "Veamos este ejemplo"
    h 'pregunta="¿Cuánto es 2+2?"\nrespuesta=4\npregunta+respuesta\nTraceback (most recent call last):\n  File "\<stdin\>", line 1, in \<module\>\nTypeError: cannot concatenate \'str\' and \'int\' objects'
    h "Para evitar estos problemas, podemos hacer una {color=#ff0}interpolación{/color} de variables"
    h 'repuesta=4\n"2+2 es \%s" respuesta\n"2+2 es 4"'
    $error=""
    $ digestivo_counter = 9
label q19:
    
    $ expresiones = ['1+1', '"1"+1', '"1"+"False"', "True + 2"]
    $ respuestas = [3,2,4,1]
    if digestivo_counter==9:
        python:
            encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[0]
            digestivo_counter=0
    elif digestivo_counter==4:
            h "Has completado esta actividad" 
    else:
        $encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[digestivo_counter]
        if check== respuestas[digestivo_counter]:
            h "Eso es correcto"
            python:
                digestivo_counter += 1
                encabezado = "Muestre el resultado de la siguiente expresión\n"+expresiones[digestivo_counter]
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
        
    return