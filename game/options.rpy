## Este archivo contiene algunas de las opciones que pueden cambiarse para
## personalizar el juego Ren'Py. Solo figuran las opciones más comunes.
## Es posible añadir muchas más personalizaciones.
##
## Las líneas que empiezan con dos marcas '#' son comentarios, no debes
## eliminar las marcas. Las líneas que comienzan con una sola marca '#'
## contienen código no activo. La marca '#' puede eliminarse si se quiere
## utilizar esa característica.

init -1 python hide:
    #persistent.console=True
    ## Esta variable habilita las herramientas de desarrollo. Debe ser
    ## ajustada a False antes del lanzamiento del juego, así el usuario
    ## no puede hacer trampas usando las herramientas de desarrollo.

    config.developer = True
    #persistent.console

    ## Control de la anchura y altura de la pantalla.

    config.screen_width = 1000
    config.screen_height = 600

    ## Título de la ventana, cuando Ren'Py se ejecuta en
    ## modo ventana.

    config.window_title = u"Programar con Python"

    ## Control del nombre y versión del juego; se utilizan en los
    ## rastreos y otras funciones de depuración.
    config.name = "Programar con Python"
    config.version = "0.0"

    #########################################
    ## Temas

    ## Para utilizar una función de tema, utilizamos themes.roundrect.
    ## Este tema configura el uso de rectángulos redondeados.
    ##
    ## La función de tema acepta una serie de parámetros que pueden
    ## personalizar la paleta de colores.

    theme.diamond(
        ## Theme: Diamond
        ## Color scheme: Kindergarten

        ## The color of an idle widget face.
        widget = "#1781b1",

        ## The color of a focused widget face.
        widget_hover = "#12678e",

        ## The color of the text in a widget.
        widget_text = "#fdfbee",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#f2edc4",

        ## The color of a disabled widget face.
        disabled = "#1ca4b2",

        ## The color of disabled widget text.
        disabled_text = "#22d5b3",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#22d5b3",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "images/background.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#ffeca6",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = True,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## Estos ajustes permiten personalizar la ventana que contiene
    ## el diálogo y la narración, reemplazándola con una imagen.

    ## Fondo de la ventana. Usando un marco ('Frame'), los dos números
    ## indican la dimensión de los bordes izquierdo/derecho y
    ## superior/inferior, respectivamente.

    # style.window.background = Frame("frame.png", 12, 12)

    ## El margen es el espacio alrededor de la ventana, en el cual el
    ## fondo no aparece.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## El 'relleno' ('padding') es el margen interior a la ventana,
    ## en el cual el fondo sí se dibuja, pero no el texto.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Altura mínima de la ventana, incluyendo margen y
    ## 'relleno'.

    # style.window.yminimum = 250


    #########################################
    ## Esta sección permite cambiar la disposición del menú principal.

    ## Colocación: Primero se establece un punto de anclaje (anchor)
    ## dentro de un elemento gràfico (displayable), y un punto de posición (pos)
    ## en la pantalla. Entonces se coloca el elemento gràfico de forma
    ## que ambos puntos coincidan.

    ## Los puntos de anclaje y de posición (anchor/pos) pueden indicarse
    ## con un número entero o decimal. Un entero indica los píxeles desde
    ## la esquina superior izquierda. Un decimal, en cambio, se interpreta
    ## como fracción de las dimensiones del elemento gráfico o la
    ## pantalla.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Personalización del tipo de letra utilizado por defecto.

    ## Archivo del tipo de letra.

    # style.default.font = "DejaVuSans.ttf"

    ## Tamaño de letra por defecto.

    # style.default.size = 22

    ## Nota: Solo cambia el tamaño de parte del texto. Otros botones
    ## tienen sus propios estilos.


    #########################################
    ## Ajuste de algunos de los sonidos utilizados
    ## por Ren'Py.

    ## Ajustar a 'False' si el juego no tiene efectos de sonido.

    config.has_sound = True

    ## Ajustar a 'False' si el juego no tiene música.

    config.has_music = True

    ## Ajustar a 'True' si el juego contiene voces.

    config.has_voice = False

    ## Sonidos utilizados cuando se hace clic en un botón o "imagemap".

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sonidos utilizados cuando se entra o sale del menú del juego.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Sonido de ejemplo utilizado para comprobar el volumen.

    # config.sample_sound = "click.wav"

    ## Música del menú principal.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Ayuda.

    ## Configuración de la opción de ayuda de los menús de Ren'Py.
    ## Puede ser:
    ## - Una etiqueta (label) en el 'script', en cuyo caso se llama esa
    ##   etiqueta para mostrar la ayuda al usuario.
    ## - El nombre de un archivo relativo al directorio base, que se abre
    ##   en un navegador web.
    ## - 'None', para deshabilitar la ayuda.
    config.help = "README.html"


    #########################################
    ## Transiciones.

    ## Desde el juego al menú del juego.
    config.enter_transition = None

    ## Desde el menú del juego al juego.
    config.exit_transition = None

    ## Entre pantallas del menú del juego.
    config.intra_transition = None

    ## Desde el menú principal al menú del juego.
    config.main_game_transition = None

    ## Desde el juego al menú principal.
    config.game_main_transition = None

    ## Desde la pantalla splash al menú principal.
    config.end_splash_transition = None

    ## Al menú principal cuando el juego ha terminado.
    config.end_game_transition = None

    ## Cuando se carga una partida.
    config.after_load_transition = None

    ## Cuando se muestra una ventana.
    config.window_show_transition = None

    ## Cuando se oculta una ventana.
    config.window_hide_transition = None

    ## Cuando se usa texto en modo NVL inmediatamente después de texto en modo ADV.
    config.adv_nvl_transition = dissolve

    ## Cuando se usa texto en modo ADV inmediatamente después de texto en modo NVL.
    config.nvl_adv_transition = dissolve

    ## Cuando se muestra la pantalla Sí/No
    config.enter_yesno_transition = None

    ## Cuando se oculta la pantalla Sí/No
    config.exit_yesno_transition = None

    ## Cuando se entra a una repetición.
    config.enter_replay_transition = None

    ## Cuando se sale de una repetición.
    config.exit_replay_transition = None

    ## Cuando la imagen cambia por una sentencia 'say' con atributos de imagen.
    config.say_attribute_transition = None

    #########################################
    ## Nombre del directorio en el cual se almacenan los datos del juego.
    ## (Debe ajustarse al inicio, antes de los otros bloques 'init', para
    ## que la información persistente pueda ser encontrada por el código 'init'.)
python early:
    config.save_directory = "Programar con Python-1455218156"

init -1 python hide:
    #########################################
    ## Valores por defecto de las Opciones

    ## Nota: Estas opciones tan solo son evaluadas la primera vez que
    ## se ejecuta un juego. Para que sean evaluadas una segunda vez,
    ## bórrese games/saves/persistent

    ## Ajusta a 'True' para comenzar en pantalla completa

    config.default_fullscreen = False

    ## Velocidad del texto por defecto en caracteres por segundo. 0 es infinito.

    config.default_text_cps = 0

    ## El ajuste de auto-avance por defecto.

    config.default_afm_time = 10

    #########################################
    ## Aquí pueden ir más personalizaciones


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Programar_con_Python-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Programar con Python"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
