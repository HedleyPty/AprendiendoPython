label n24:
    h "Ahora vamos a ver como funciona el control de flujo"
    h "Primero imaginemos que manejamos un carro y nos encontramos un semáforo en rojo"
    h "De repente la luz cambia a verde, lo que indica que podemos avanzar"
    h "Dentro de un programa una {color=#ff0}toma de decisión{/color} se ejecuta automáticamente cuando una o más variables cambian de estado"
    h "El control de flujo, implica una serie de acción que ocurren cuando una variable toma un determinado valor"
    h "El control de flujo en Python se realiza mediante {color=#ff0}bloques{/color} cuando una {color=#ff0}condición{/color} es {color}cierta{/color}"
    h "Las palabras reservadas que delimitan el {color=#ff0}control de flujo{/color} son {color=#ff0}if{/color}, {color=#ff0}else{/color}, {color=#ff0}elif{/color} y {color=#ff0}while{/color}"
    h "Comenzamos por la palabra reservada {color=#ff0}if{/color} que significa en español {color=#ff0}si{/color}"
    h "Hay dos formas de crear un control de flujo con {color=#ff0}if{/color}: con una línea o con un bloque"
    h "Para crear una línea, escribimos la palabra reservada {color=#ff0}if{/color} seguida por una condición (que debe ser cierta para que se ejecute la línea)\nluego dos puntos {color=#ff0}seguido de la acción a ejecutar{/color}"
    h "Si la condición no se cumple, el código despues de los dos puntos {color=#ff0}:{/color} no se ejecuta"
    consola "{color=#f0f}#Versión Python 2, como a >20 es falso, el código no se ejecuta{/color}a=14\nb=2\nif a>20: print b"
    consola "{color=#f0f}#Versión Python 2, como a >20 es cierto, el código se ejecuta{/color}a=24\nb=2\nif a>20: print b\n2"
    consola "{color=#f0f}#Versión Python 3, como a >20 es falso, el código no se ejecuta{/color}a=14\nb=2\nif a>20: print (b)"
    consola "{color=#f0f}#Versión Python 3, como a >20 es cierto, el código se ejecuta{/color}a=24\nb=2\nif a>20: print (b)\n2"
    h "Si queremos ejecutar más de una línea necesitamos un {color=#ff0}bloque{/color}"
    h "El bloque es una serie de líneas que tienen {color=#ff0}sangría{/color} adicicional despues de la sentencia que inicia con if"
    h "El bloque termina en la última línea con {color=#ff0}sangría{/color}"
    h "En este tutorial he usado bloques {color=#ff0}if{/color} para valorar si sus respuestas son correctas o no"
    #Buscar las líneas
    h "Pueden ver esto en la página github de este proyecto{a}https://github.com/HedleyPty/AprendiendoPython{/a} en las líneas ..."
    consola '{color=#f0f}#Esto ocurre cada vez que responden en los ejercicios{/color}if check == respuestas\[counter\]:\n    counter += 1\n    if counter ==3:\n    jump proxCapitulo'
    
    
    h "Además del control de flujo con else que significa {color=#ff0}sino{/color}"
    
    h "La sentencia y los bloque else se escribe de la misma manera que la sentenc"