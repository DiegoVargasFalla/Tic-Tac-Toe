import flet
import time
import pygame
import os
import sys

from flet import (
    Container,
    Text,
    IconButton,
    Icon,
    Column,
    Row,
    BoxShadow,
    FontWeight,
    AlertDialog,
    TextField,
    Checkbox,
    Audio
)

#class for player 
class Player:

    def __init__(self):

        self.name = ""
        self.shift = False
        self.game_won = 0
        self.figure = ""

    # metodo para retornar el turno del jugador
    def get_shift(self):
        return self.shift
    
    # metodo para ingresar el turno del jugador 
    def set_shitf(self, shift):
        self.shift = shift

    # metodo para ingresar el nombre del jugador
    def get_name(self):
        return self.name
    
    # metodo para ingresar el noombre del usuario
    def set_name(self, name):
        self.name = name

    # method para retornar el numero de juegos ganados del jugador
    def get_game_won(self):
        return self.game_won
    
    # metodo para ingresar el numero de juegos ganados
    def set_game_won(self, num):
        self.game_won += num

    # metodos para obtener que figura tiene el jugador
    def get_figure(self):
        return self.figure
    
    # metodo para ingresar la figura que tiene el jugaodr
    def set_figure(self, figure):
        self.figure = figure

    # metodo oara ver la informacion del jugador
    def get_info_player(self, jugador):
        print(f"- {jugador}\n   - Nombre: {self.name}\n   - turno: {self.shift}\n   - juegos ganados: {self.game_won}\n   - figura: {self.figure}")

    
# clase para la interfaz grafica
class Gui_app:

    def __init__(self, page):

        self.page = page

        pygame.init()
        pygame.mixer.init()

        self.sound_win = pygame.mixer.Sound("assets/sound_win.wav")
        self.audio_error = pygame.mixer.Sound("assets/error_start.wav")
        self.audio_start_game = pygame.mixer.Sound("assets/start_game.wav")
        self.sound_triki = pygame.mixer.Sound("assets/sound_triki.wav")
        self.audio_click_container = pygame.mixer.Sound("assets/click_container.wav")

        # variable para cuando el jugador quiera cambiar los valores de los nombres saber que conteneddor se esta editando 
        self.num_clean_widgets = 0

        # variable para que cuando se ingresen los nombres de los jugadores se pueda iniciar el juego con el boton start
        self.playing = False

        # variable para activar el juego y se pueda dar click en los contenedores de cada figura
        self.click_start = False

        # variable para saber cual fue el gandor de una partida
        self.triki_player1 = False
        self.triki_player2 = False

        # variable para contar las partidas que se van jugando
        self.count_games_num = 0

        #< variable para cuando el jugador quiera ingresar el nombre saber que contenedor se esta editando
        self.edit_name = 0

        # se instancian dos jugadores para utilizar los metodos anteriore en la clase player
        self.player_1 = Player()
        self.player_2 = Player()

        # se deja por defecto el turno del jugador 1 en verdadero para que siempre que se incicie el juego 
        # sea el primero en jugar, esto para facilitar el manejo de los turnos
        self.player_1.set_shitf(True)
        self.player_2.set_shitf(False)

        # tamaño de la ventana
        self.page.window.height = 520
        self.page.window.width = 680

        #  maximo tamaño de la ventana
        self.page.window.max_width = 680
        self.page.window.max_height = 520

        # minimo tmaño de laventana
        self.page.window.min_width = 680
        self.page.window.min_height = 520

        # ubucacion de la ventana
        self.page.window.center()

        
        # texto para el numero de juegos que se van a jugar
        self.games_num = Text(
            "0",
            weight=FontWeight.W_500,
            color="white"
        )

        # conteo de juegos que se an jugado 
        self.games_count = Text(
            "0",
            weight=FontWeight.W_500,
            color="white"
        )

        # palabra en  emdio de el numero de juegos y el numero de juegos jugados
        self.text_of = Text(
            "of",
            weight=FontWeight.W_500,
            color="white"
        )

        # nombre del juggador 1
        self.text_player_1 = Text(
                        "Player 1", 
                        weight=FontWeight.W_700
                    )
        
        # nombre de jugador 2
        self.text_player_2 = Text(
                        "Player 2",
                        weight=FontWeight.W_700
                    )
        
        # numero de juegos ganados jugador 1
        self.games_won_P1 = Text(
            "0",
            weight=FontWeight.W_500
        )

        # # numero de juegos ganados jugador 2
        self.games_won_P2 = Text(
            "0",
            weight=FontWeight.W_500
        )

        # figura de jugador 1
        self.figure_P1 = Text(
            "",
            weight=FontWeight.W_700,
            size=20
        )

        # figura jugador 2
        self.figure_P2 = Text(
            "",
            weight=FontWeight.W_700,
            size=20
        )

        # aqui estara el texto de el nombe y demas del jugador 1
        self.row_player_1 = Row(
            controls=[
                self.figure_P1,
                self.text_player_1,
                self.games_won_P1,
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )
        
         # aqui estara el texto de el nombe y demas del jugador 2
        self.row_player_2 = Row(
            controls=[
                self.figure_P2,
                self.text_player_2,
                self.games_won_P2
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )
        
        # este es el contenedor 1 que estara ubicado en la parte superior izquierda donde estan todos los recuadros.
        # de aqui en edelannte hasta el contenedor 9 son todos iguales y con la misma funcion
        self.container_1 = Container(
            margin=flet.margin.only(top=0, bottom=-4, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[1, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_2 = Container(
            margin=flet.margin.only(top=0, bottom=-4, right=-4),
            bgcolor="red",
            image_src="",
            image_fit="FILL",
            width=100,
            height=100,
            border_radius=10,
            ink=True,
            data=[2, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_3 = Container(
            margin=flet.margin.only(top=0, bottom=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[3, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )
        

        self.container_4 = Container(
           margin=flet.margin.only(top=0, bottom=-4, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[4, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_5 = Container(
            margin=flet.margin.only(top=0, bottom=-4, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[5, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_6 = Container(
            margin=flet.margin.only(top=0, bottom=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[6, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_7 = Container(
            margin=flet.margin.only(top=0, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[7, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_8 = Container(
            margin=flet.margin.only(top=0, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[8, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        self.container_9 = Container(
            margin=flet.margin.only(top=0, bottom=0),
            bgcolor="red",
            width=100,
            height=100,
            image_src="",
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=[9, False],
            on_click=lambda e: self.play(e.control.data),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            ),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=2,
                color="#c5c5d8",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
            )
        )

        # contenedor donde se dara ell click para ingresar el nombre del jugador 1
        self.container_player_1 = Container(
            bgcolor="#f4faf5",
            content=self.row_player_1,
            width=150,
            height=30,
            on_click=lambda e: self.open_dialog(e.control.data),
            ink=True,
            border_radius=10,
            data='1',
        )

        # contenedor donde se dara ell click para ingresar el nombre del jugador 2
        self.container_player_2 = Container(
            bgcolor="#f4faf5",
            content=self.row_player_2,
            width=150,
            height=30,
            on_click=lambda e: self.open_dialog(e.control.data),
            border_radius=10,
            data='2',
        )

        # fila para pner los dos contenedores de forma horizontal consecutiva
        self.row_data = Row(
            controls=[
                self.container_player_1,
                self.container_player_2
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        # este contenedor contiene el boton de iniciar el juego
        self.container_play = Container(
            bgcolor="#26994e",
            width=90,
            height=28,
            border_radius=10,
            ink=True,
            on_click=self.check_star,
            content=Row(
                        spacing=5,
                        controls=[
                            Icon(name="PLAY_CIRCLE", color="white", size=23),
                            Text("Start", weight=FontWeight.W_700, color="white")
                        ],
                        alignment=flet.MainAxisAlignment.CENTER
                    )
                )

        # contenedor para mostrar el numero de juegos que van y el numero de juegos que se van a jugar
        self.container_num_games = Container(
            bgcolor="#26994e",
            width=105,
            height=28,
            border_radius=10,
            on_click="",
            content=Row(
                        spacing=5,
                        controls=[
                            Text("Games", weight=FontWeight.W_700, color="white"),
                            self.games_count,
                            self.text_of,
                            self.games_num
                        ],
                        alignment=flet.MainAxisAlignment.CENTER
                    )
                )
        
        # fila que contiene los dos contenedores de numero de juegos y start
        self.row_container_play = Row(
            spacing=20,
            controls=[
                Column(width=70),
                self.container_num_games,
                self.container_play
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        # de aqu en adelante hasta la fila 3 estaran los contenedores donde se mostraran las figuras del juego
        # cada fila tiene 3 contenedores
        self.row_1 = Row(
            controls=[
                self.container_1,
                self.container_2,
                self.container_3
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        self.row_2 = Row(
            controls=[
                self.container_4,
                self.container_5,
                self.container_6
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        self.row_3 = Row(
            controls=[
                self.container_7,
                self.container_8,
                self.container_9
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        # este container tiene las tres filas de los contenedores de la figuras, organizadas en una columna para que se vean 3 filas 3 columnas
        self.container_all = Container(
            bgcolor="transparent",
            # expand=True,
            #margin=-10,
            #height=self.page.height,
            content=Column(
                controls=[
                    self.row_1,
                    self.row_2,
                    self.row_3,
                ],
                alignment=flet.MainAxisAlignment.CENTER
            )
        )

        # esta columna tiene los tres containers que estan de arriba hacia abajo, en tres secciones, una la informacion del jugador, otra es la 
        # de el recuadro de los juegos que van y un boton de start
        self.column_all = Column(
            spacing=10,
            controls=[
                self.row_data,
                self.row_container_play,
                self.container_all,
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        # este es el container principal, que es el que contiene todo lo anteriro y de fondo tiene una imagen
        self.firstContainer = Container(
            bgcolor="green",
            image_src="bground.png",
            image_fit="FILL",
            content=self.column_all,
            expand=True,
            ink=True,
            on_click=lambda e: print(""),
            height=self.page.height,
            # width=self.page.width,
            margin=-10,
        )

        # esto estara en la ventana emergente que se muestra cuando se da click en el contenedor de el nombre
        self.input_name_p1 = TextField(
            width=180,
            label="Name player 1",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        # aqui se ingresan el numero de partidas que se jugaran
        self.input_num_game = TextField(
            width=50,
            #height=25,
            label="N°",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        # esto estara en la ventana emergente que se muestra cuando se da click en el contenedor de el nombre
        self.input_name_p2 = TextField(
            width=230,
            label="Name player 2",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        # aqui se elige la figura que desee el jugador
        self.check_x_p1 = Checkbox(
            label="X",
            active_color="#095b2d"
        )

        # aqui se elige la figura que desee el jugador
        self.check_o_p1 = Checkbox(
            label="O",
            active_color="#095b2d"
        )

        # aqui se elige la figura que desee el jugador
        self.check_x_p2 = Checkbox(
            label="X",
            active_color="#095b2d"
        )

        # aqui se elige la figura que desee el jugador
        self.check_o_p2 = Checkbox(
            label="O",
            active_color="#095b2d"
        )

        # esta es la ventana emergente para ingresar la informacion del jugador 1
        self.dialog_names_p1 = AlertDialog(
            modal=True,
            bgcolor="#a7c2ad",
            title=Text("Welcome", weight=FontWeight.W_700),
            actions=[]
        )

         # esta es la ventana emergente para ingresar la informacion del jugador 2
        self.dialog_names_p2 = AlertDialog(
            modal=True,
            bgcolor="#a7c2ad",
            title=Text("Welcome", weight=FontWeight.W_700),
        )

        # este boton es para cerrar la ventana emergente y confirmar la informacion ingresada
        self.button_check = IconButton(
                                    icon="CHECK_CIRCLE_ROUNDED",
                                    icon_color="#095b2d",
                                    icon_size=30,
                                    on_click=self.close_dialog
                                    )
        
        # boton para limpiar la informacion del jugador.
        self.button_clean = IconButton(
                                    icon="DELETE_SWEEP_ROUNDED",
                                    icon_color="#da132c",
                                    icon_size=30,
                                    on_click=self.clean_widgets_info
                                    )
        
        # esta lista tiene todos los contenedores, es para poder manejar los eventos de una manera mas facil
        self.list_containers = [
            self.container_1, self.container_2, self.container_3,
            self.container_4, self.container_5, self.container_6,
            self.container_7, self.container_8, self.container_9
        ]

    @staticmethod
    def resolver_ruta(ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

    # metodo para que los contenedores de los nombres sean intermitentes si no se ingresan los nombres
    def change_color_names(self):

        while True:

            if self.text_player_1.value == "Player 1" and self.text_player_2.value == "Player 2":
              
                self.container_player_1.shadow = ""
                self.page.update()
                self.container_player_2.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
                self.page.update()

                time.sleep(0.3)

                self.container_player_1.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
                self.page.update()
                self.page.update()

                self.container_player_2.shadow = ""
                self.page.update()
                time.sleep(0.3)

            elif self.text_player_1.value != "Player 1" and self.text_player_2.value != "Player 2":

                self.container_player_1.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )

                self.container_player_2.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
                self.page.update()
                break

            elif self.text_player_1.value == "Player 1":

                self.container_player_1.shadow = ""
                self.page.update()

                time.sleep(0.3)

                self.container_player_1.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
                self.page.update()
                time.sleep(0.3)
            elif self.text_player_2.value == "Player 2":

                self.container_player_2.shadow = ""
                self.page.update()

                time.sleep(0.3)

                self.container_player_2.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#a7c2ad",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
                self.page.update()
                time.sleep(0.3)

    # metodo para limpiar la informacion de la ventana emergente si se quiere cambiar el nombre
    def clean_widgets_info(self, e):

        if self.num_clean_widgets == 1:
            self.figure_P1.value = ""
            self.figure_P2.value = ""
            self.input_name_p1.value = ""
            self.input_num_game.value = ""
            self.check_x_p1.disabled = False
            self.check_x_p1.value = False
            self.check_o_p1.disabled = False
            self.check_o_p1.value = False

            self.check_x_p2.disabled = False
            self.check_x_p2.value = False
            self.check_o_p2.disabled = False
            self.check_o_p2.value = False
            self.click_start = False

            self.container_play.shadow = BoxShadow(
                                                spread_radius=3,
                                                blur_radius=5,
                                                color="transparent",
                                                offset=flet.Offset(0, 0),
                                                blur_style=flet.ShadowBlurStyle.NORMAL,
                                            )
            self.page.update()

        elif self.num_clean_widgets == 2:

            self.figure_P2.value = ""
            self.figure_P1.value = ""
            self.input_name_p2.value = ""
            self.check_x_p2.disabled = False
            self.check_x_p2.value = False
            self.check_o_p2.disabled = False
            self.check_o_p2.value = False

            self.check_x_p1.disabled = False
            self.check_x_p1.value = False
            self.check_o_p1.disabled = False
            self.check_o_p1.value = False
            self.click_start = False

            self.container_play.shadow = BoxShadow(
                                                spread_radius=3,
                                                blur_radius=5,
                                                color="transparent",
                                                offset=flet.Offset(0, 0),
                                                blur_style=flet.ShadowBlurStyle.NORMAL,
                                            )
            
            self.page.update()

    # este metodo abre la ventana emergente de la informacion
    def open_dialog(self, e):
        if e == '1':

            self.edit_name = 1
            self.num_clean_widgets = 1

            self.dialog_names_p1.content = Container(
                                                bgcolor="transparent",
                                                height=50,
                                                ink=True,
                                                content=Row(
                                                    controls=[
                                                        self.input_name_p1,
                                                        self.input_num_game
                                                        ]
                                                    )
                                                )
            self.dialog_names_p1.actions = Row(
                                            controls=[
                                                    self.check_x_p1, 
                                                    self.check_o_p1,
                                                    Column(width=25),
                                                    self.button_clean,
                                                    self.button_check,
                                            ],
                                            alignment=flet.MainAxisAlignment.SPACE_AROUND
                                        ),
            self.page.overlay.append(self.dialog_names_p1)
            self.page.update()
            self.dialog_names_p1.open = True
            self.page.update()

        elif e == '2':

            self.edit_name = 2
            self.num_clean_widgets = 2

            self.dialog_names_p2.content = Container(
                                                bgcolor="transparent",
                                                height=50,
                                                ink=True,
                                                content=Row(
                                                    controls=[
                                                        self.input_name_p2
                                                        ]
                                                    )
                                                )
            self.dialog_names_p2.actions = Row(
                                            controls=[
                                                    self.check_x_p2, 
                                                    self.check_o_p2,
                                                    Column(width=25),
                                                    self.button_clean,
                                                    self.button_check,
                                            ],
                                            alignment=flet.MainAxisAlignment.SPACE_AROUND
                                        ),
            self.page.overlay.append(self.dialog_names_p2)
            self.page.update()
            self.dialog_names_p2.open = True
            self.page.update()

    # metodo para guardar la informacion y cerrar la ventana emergente
    def close_dialog(self, e):

        if self.input_name_p1.value and self.input_name_p2.value and self.input_num_game.value:
            self.container_play.shadow = BoxShadow(
                                                spread_radius=3,
                                                blur_radius=5,
                                                color="#3ccd6e",
                                                offset=flet.Offset(0, 0),
                                                blur_style=flet.ShadowBlurStyle.NORMAL,
                                            )
            self.playing = True

        if self.edit_name == 1 and self.input_name_p1.value and self.input_num_game.value:

            if self.check_x_p1.value and self.check_o_p1.value:

                for l in range(1, 3):

                    self.check_o_p1.value = False
                    self.check_x_p1.value = False
                    self.page.update()
                    time.sleep(0.1)
                    self.check_o_p1.value = True
                    self.check_x_p1.value = True
                    self.page.update()
                    time.sleep(0.1)
                
                self.check_o_p1.value = False
                self.check_x_p1.value = False
                self.page.update()

            elif self.check_x_p1.value or self.check_o_p1.value:

                self.text_player_1.value = self.input_name_p1.value.capitalize()
                self.dialog_names_p1.open = False

                self.player_1.set_name(self.input_name_p1.value)
                # self.player_1.set_shitf(True)

                if self.check_x_p1.value and not self.check_o_p1.value:
                    self.check_x_p2.disabled = True
                    self.check_o_p2.value = True
                    self.player_1.set_figure("X")
                    self.figure_P1.value = self.player_1.get_figure()
                    

                elif self.check_o_p1.value and not self.check_x_p1.value:
                    self.check_o_p2.disabled = True
                    self.check_x_p2.value = True
                    self.player_1.set_figure("O")
                    self.figure_P1.value = self.player_1.get_figure()

                self.player_1.get_info_player("PLAYER 1")

                self.dialog_names_p1 = AlertDialog(
                                                modal=True,
                                                bgcolor="#9bb9a8",
                                                title=Text("Welcome", weight=FontWeight.W_700),
                                                actions=[]
                                                )
                self.games_num.value = self.input_num_game.value
                self.page.update()

            elif not self.check_o_p1.value and not self.check_x_p1.value:

                for j in range(1, 4):

                    self.check_o_p1.value = True
                    self.check_x_p1.value = True
                    self.page.update()
                    time.sleep(0.1)
                    self.check_o_p1.value = False
                    self.check_x_p1.value = False
                    self.page.update()
                    time.sleep(0.1)

                self.check_o_p1.value = False
                self.check_x_p1.value = False
                self.page.update()

        elif self.edit_name == 2 and self.input_name_p2.value:

            if self.check_x_p2.value and self.check_o_p2.value:

                for l in range(1, 3):
                    self.check_o_p2.value = False
                    self.check_x_p2.value = False
                    self.page.update()
                    time.sleep(0.1)
                    self.check_o_p2.value = True
                    self.check_x_p2.value = True
                    self.page.update()
                    time.sleep(0.1)

                self.check_o_p2.value = False
                self.check_x_p2.value = False
                self.page.update()

            elif self.check_x_p2.value or self.check_o_p2.value:

                self.text_player_2.value = self.input_name_p2.value.capitalize()
                self.dialog_names_p2.open = False

                self.player_2.set_name(self.input_name_p2.value)
                # self.player_2.set_shitf(True)

                if self.check_x_p2.value and not self.check_o_p2.value:
                    self.check_x_p1.disabled = True
                    self.check_o_p1.value = True
                    self.player_2.set_figure("X")
                    self.figure_P2.value = self.player_2.get_figure()
                elif self.check_o_p2.value and not self.check_x_p2.value:
                    self.check_o_p1.disabled = True
                    self.check_x_p1.value = True
                    self.player_2.set_figure("O")
                    self.figure_P2.value = self.player_2.get_figure()
                self.player_2.get_info_player("PLAYER 2")
                
                self.dialog_names_p2 = AlertDialog(
                                                modal=True,
                                                bgcolor="#9bb9a8",
                                                title=Text("Welcome", weight=FontWeight.W_700),
                                                actions=[]
                                                )
                self.page.update()

            elif not self.check_x_p2.value and not self.check_o_p2.value:

                    for j in range(1, 4):

                        self.check_o_p2.value = True
                        self.check_x_p2.value = True
                        self.page.update()
                        time.sleep(0.1)
                        self.check_o_p2.value = False
                        self.check_x_p2.value = False
                        self.page.update()
                        time.sleep(0.1)
        
        else:
            if self.edit_name == 1:

                if not self.input_name_p1.value and not self.input_num_game.value:
                    for i in range(1, 6):

                        self.input_name_p1.border_color = flet.colors.ERROR
                        self.input_num_game.border_color = flet.colors.ERROR
                        self.page.update()
                        time.sleep(0.1)
                        self.input_name_p1.border_color = "white"
                        self.input_num_game.border_color = "white"
                        self.page.update()
                        time.sleep(0.1)
                    
                elif self.input_name_p1.value and not self.input_num_game.value:
                    for i in range(1, 6):

                        self.input_num_game.border_color = flet.colors.ERROR
                        self.page.update()
                        time.sleep(0.1)
                        self.input_num_game.border_color = "white"
                        self.page.update()
                        time.sleep(0.1)

                elif not self.input_name_p1.value and self.input_num_game.value:
                    for i in range(1, 6):

                        self.input_name_p1.border_color = flet.colors.ERROR
                        self.page.update()
                        time.sleep(0.1)
                        self.input_name_p1.border_color = "white"
                        self.page.update()
                        time.sleep(0.1)

            elif not self.input_name_p2.value and self.edit_name == 2:

                for j in range(1, 7):
                    self.input_name_p2.border_color = flet.colors.ERROR
                    self.page.update()
                    time.sleep(0.1)
                    self.input_name_p2.border_color = "white"
                    self.page.update()
                    time.sleep(0.1)

    # metodo para limpipar las figuras de cada contenedor
    def clean_table(self):
        time.sleep(1.5)

        for i in self.list_containers:

            if i.image_src and i.data[1]:
                i.image_src = ""
                i.data[1] = False
                time.sleep(0.090)
                self.page.update()
        
        self.triki_player1 = False
        self.triki_player2 = False

    # metodo que limpia todaa la informacion y las figuras cuando se termina el juago
    def clean_table_and_widgets(self):
        time.sleep(1.5)

        for i in self.list_containers:

            if i.image_src and i.data[1]:
                i.image_src = ""
                i.data[1] = False
                time.sleep(0.090)
                self.page.update()

        self.games_count.value = "0"
        self.games_num.value = "0"
        self.playing = False
        self.click_start = False
        
        self.text_player_1.value = "Player 1"
        self.input_name_p1.value = ""
        self.figure_P1.value = ""
        self.games_won_P1.value = ""
        self.check_o_p1.value = False
        self.check_x_p1.value = False
        self.input_num_game.value = ""
        self.check_o_p1.disabled = False
        self.check_x_p1.disabled = False
        self.player_1.game_won = 0

        self.text_player_2.value = "Player 2"
        self.input_name_p2.value = ""
        self.figure_P2.value = ""
        self.games_won_P2.value = ""
        self.check_o_p2.value = False
        self.check_x_p2.value = False
        self.check_o_p2.disabled = False
        self.check_x_p2.disabled = False
        self.player_2.game_won = 0

        self.count_games_num = 0

        self.triki_player1 = False
        self.triki_player2 = False
        self.page.update()
        self.change_color_names()

    # ventana emergente cuando se acaba el juego y muestra el nombre del jugador
    def dialog_win(self, name):
        
        dialog_win = AlertDialog(
            modal=False,
            bgcolor="transparent",
            content=Container(
                bgcolor="green",
                # padding=20,
                border_radius=30,
                width=200,
                height=200,
                content=Column(
                    spacing=-15,
                    controls=[
                        Row(
                            controls=[
                                Container(
                                        border_radius=50,
                                        margin=flet.margin.only(top=15),
                                        bgcolor="transparent",
                                        width=43,
                                        content=Row(
                                            controls=[
                                                    Icon(
                                                        name="STAR_ROUNDED", 
                                                        size=40,
                                                        color="#9ca51a"
                                                        )
                                                    ],
                                                    alignment=flet.MainAxisAlignment.CENTER
                                                ),
                                            shadow=BoxShadow(
                                                            spread_radius=0,
                                                            blur_radius=13,
                                                            color="#cfd519",
                                                            offset=flet.Offset(0, 0),
                                                            blur_style=flet.ShadowBlurStyle.NORMAL,
                                                ),
                                            ),
                                            Container(
                                                border_radius=50,
                                                margin=flet.margin.only(top=-40),
                                                bgcolor="transparent",
                                                width=43,
                                                content=Row(
                                                controls=[
                                                        Icon(
                                                            name="STAR_ROUNDED", 
                                                            size=40,
                                                            color="#9ca51a"
                                                            )
                                                        ],
                                                        alignment=flet.MainAxisAlignment.CENTER
                                                    ),
                                                shadow=BoxShadow(
                                                                spread_radius=0,
                                                                blur_radius=13,
                                                                color="#cfd519",
                                                                offset=flet.Offset(0, 0),
                                                                blur_style=flet.ShadowBlurStyle.NORMAL,
                                                            ),
                                            ),
                                            Container(
                                                border_radius=50,
                                                margin=flet.margin.only(top=15),
                                                bgcolor="transparent",
                                                width=43,
                                                content=Row(
                                                controls=[
                                                        Icon(
                                                            name="STAR_ROUNDED", 
                                                            size=40,
                                                            color="#9ca51a"
                                                            )
                                                        ],
                                                        alignment=flet.MainAxisAlignment.CENTER
                                                    ),
                                                shadow=BoxShadow(
                                                                spread_radius=0,
                                                                blur_radius=13,
                                                                color="#cfd519",
                                                                offset=flet.Offset(0, 0),
                                                                blur_style=flet.ShadowBlurStyle.NORMAL,
                                                            ),
                                            ),
                                        ],
                                        alignment=flet.MainAxisAlignment.SPACE_AROUND
                                ),
                        Row(
                            controls=[
                                Text(
                                    f"WINNER",
                                    weight=FontWeight.BOLD,
                                    size=35,
                                    ),
                            ],
                            alignment=flet.MainAxisAlignment.CENTER
                        ),
                        Row(
                            controls=[
                                Text(
                                    f"{name}",
                                    weight=FontWeight.BOLD,
                                    size=35,
                                    ),
                            ],
                            alignment=flet.MainAxisAlignment.CENTER
                        )
                    ],
                    alignment=flet.MainAxisAlignment.CENTER
                ),
                gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#51b373", "#277c85", "#053c42"],
            ),
            shadow=BoxShadow(
                spread_radius=3,
                blur_radius=12,
                color="#51b373",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.NORMAL,
                ),
            ),
        )
        self.page.overlay.append(dialog_win)
        self.page.update()
        dialog_win.open = True
        self.sound_win.play()

    # ventana emergente si quedaron empate los jugadores
    def empate(self, name1, name2):
        
        dialog_win = AlertDialog(
                                modal=False,
                                bgcolor="transparent",
                                content=Container(
                                    bgcolor="green",
                                    # padding=20,
                                    border_radius=30,
                                    width=200,
                                    height=200,
                                    content=Column(
                                        spacing=-15,
                                        controls=[
                                            Row(
                                                controls=[
                                                    Text(
                                                        f"DRAW",
                                                        weight=FontWeight.BOLD,
                                                        size=35,
                                                        color="white"
                                                        ),
                                                ],
                                                alignment=flet.MainAxisAlignment.CENTER
                                            ),
                                            Row(
                                                spacing=10,
                                                controls=[
                                                    Text(
                                                        f"{name1} - ",
                                                        weight=FontWeight.BOLD,
                                                        size=28,
                                                        ),
                                                    Text(
                                                        f"{name2}",
                                                        weight=FontWeight.BOLD,
                                                        size=28,
                                                        ),
                                                ],
                                                alignment=flet.MainAxisAlignment.CENTER
                                            )
                                        ],
                                        alignment=flet.MainAxisAlignment.CENTER
                                    ),
                                    gradient=flet.LinearGradient(
                                    begin=flet.alignment.top_center,
                                    end=flet.alignment.bottom_center,
                                    colors=["#51b373", "#277c85", "#053c42"],
                                ),
                                shadow=BoxShadow(
                                    spread_radius=3,
                                    blur_radius=12,
                                    color="#51b373",
                                    offset=flet.Offset(0, 0),
                                    blur_style=flet.ShadowBlurStyle.NORMAL,
                                    ),
                                ),
                            )
        self.page.overlay.append(dialog_win)
        self.page.update()
        dialog_win.open = True
        self.page.update()
        self.sound_win.play()

    # metodo cuando hay un ganador de una partida, esta funcion muestra la linea que se cruza cuando hay un tic tac toe
    def triki(self, num1, num2, num3, image):


        self.sound_triki.play()


        self.list_containers[int(num1)].image_src = image
        self.page.update()
        time.sleep(0.1)

        self.list_containers[int(num2)].image_src = image
        self.page.update()
        time.sleep(0.1)

        self.list_containers[int(num3)].image_src = image
        self.page.update()

        self.count_games_num += 1
        self.games_count.value = self.count_games_num

        if self.triki_player1:
            # mostrar que a sido el ganador
            self.player_1.set_game_won(1) 
            self.games_won_P1.value = self.player_1.get_game_won()
            self.page.update()

            if self.count_games_num == int(self.games_num.value)  and self.player_1.get_game_won() > self.player_2.get_game_won():
                self.dialog_win(self.text_player_1.value)
                self.clean_table_and_widgets()
            elif self.count_games_num == int(self.games_num.value) and self.player_2.get_game_won() == self.player_1.get_game_won():
                self.empate(self.player_1.get_name(), self.player_2.get_name())
                self.clean_table_and_widgets()
            elif self.count_games_num == int(self.games_num.value)  and self.player_1.get_game_won() < self.player_2.get_game_won():
                self.dialog_win(self.text_player_2.value)
                self.clean_table_and_widgets()
            elif self.count_games_num < int(self.games_num.value):
                self.clean_table()
            else:
                pass

        elif self.triki_player2:
            # mostrar ganador jugador 2
            self.player_2.set_game_won(1)

            self.games_won_P2.value = self.player_2.get_game_won()
            self.page.update()

            if self.count_games_num == int(self.games_num.value) and self.player_2.get_game_won() > self.player_1.get_game_won():
                self.dialog_win(self.text_player_2.value)
                self.clean_table_and_widgets()
            elif self.count_games_num == int(self.games_num.value) and self.player_2.get_game_won() == self.player_1.get_game_won():
                self.empate(self.player_1.get_name(), self.player_2.get_name())
                self.clean_table_and_widgets()
            elif self.count_games_num == int(self.games_num.value)  and self.player_1.get_game_won() > self.player_2.get_game_won():
                self.dialog_win(self.text_player_1.value)
                self.clean_table_and_widgets()
            elif self.count_games_num < int(self.games_num.value):
                self.clean_table()
            else:
                pass

    # este metodo es la que cambia la figura de un contenedor cuando se le da click
    def play(self, e):

        if self.text_player_1.value != "Player 1" and self.text_player_2.value != "Player 2" and self.click_start and not e[1]:

            if self.player_1.get_shift() and not self.player_2.get_shift():
  
                for i in self.list_containers:
    
                    if i.data[0] == e[0] and not i.image_src and self.player_1.get_figure() == "X":

                        i.image_src = "X_img.png"
                        self.audio_click_container.play()
                        i.data[1] = True
                        self.page.update()

                        self.container_player_2.shadow = BoxShadow(
                            spread_radius=7,
                            blur_radius=20,
                            color="#3bcc4f",
                            offset=flet.Offset(0, 0),
                            blur_style=flet.ShadowBlurStyle.NORMAL,
                        )
                        self.container_player_1.shadow = BoxShadow(
                                spread_radius=7,
                                blur_radius=20,
                                color="",
                                offset=flet.Offset(0, 0),
                                blur_style=flet.ShadowBlurStyle.NORMAL,
                            )
                        self.page.update()

                        self.player_1.set_shitf(False)
                        self.player_2.set_shitf(True)

                    elif i.data[0] == e[0] and not i.image_src and self.player_1.get_figure() == "O":
                        i.image_src = "O_img.png"
                        self.audio_click_container.play()
                        i.data[1] = True
                        self.page.update()

                        self.container_player_2.shadow = BoxShadow(
                            spread_radius=7,
                            blur_radius=20,
                            color="#3bcc4f",
                            offset=flet.Offset(0, 0),
                            blur_style=flet.ShadowBlurStyle.NORMAL,
                        )
                        self.container_player_1.shadow = BoxShadow(
                                spread_radius=7,
                                blur_radius=20,
                                color="",
                                offset=flet.Offset(0, 0),
                                blur_style=flet.ShadowBlurStyle.NORMAL,
                            )
                        self.page.update()

                        self.player_1.set_shitf(False)
                        self.player_2.set_shitf(True)

            elif self.player_2.get_shift() and not self.player_1.get_shift():

                for j in self.list_containers:

                    if j.data[0] == e[0] and not j.image_src and self.player_2.get_figure() == "X":

                        j.image_src = "X_img.png"
                        self.audio_click_container.play()
                        j.data[1] = True

                        self.page.update()

                        self.container_player_1.shadow = BoxShadow(
                            spread_radius=7,
                            blur_radius=20,
                            color="#3bcc4f",
                            offset=flet.Offset(0, 0),
                            blur_style=flet.ShadowBlurStyle.NORMAL,
                        )
                        self.container_player_2.shadow = BoxShadow(
                                spread_radius=7,
                                blur_radius=20,
                                color="",
                                offset=flet.Offset(0, 0),
                                blur_style=flet.ShadowBlurStyle.NORMAL,
                            )
                        self.page.update()

                        self.player_1.set_shitf(True)
                        self.player_2.set_shitf(False)

                    elif j.data[0] == e[0] and not j.image_src and self.player_2.get_figure() == "O":
    
                        j.image_src = "O_img.png"
                        self.audio_click_container.play()
                        j.data[1] = True
                        self.page.update()

                        self.container_player_1.shadow = BoxShadow(
                            spread_radius=7,
                            blur_radius=20,
                            color="#3bcc4f",
                            offset=flet.Offset(0, 0),
                            blur_style=flet.ShadowBlurStyle.NORMAL,
                        )
                        self.container_player_2.shadow = BoxShadow(
                                spread_radius=7,
                                blur_radius=20,
                                color="",
                                offset=flet.Offset(0, 0),
                                blur_style=flet.ShadowBlurStyle.NORMAL,
                            )
                        self.page.update()
                        self.player_1.set_shitf(True)
                        self.player_2.set_shitf(False)


        else:
            # reproducir audio de error
            self.audio_error.play()

        # de aqui hasta el ultimo conticional, son las verificaciones si hay tic tac toe
        
        if self.list_containers[0].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(0, 4, 8, "x_left_img.png")
            

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[3].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(0, 3, 6, "x_center_img.png")
        
        elif self.list_containers[1].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(1, 4, 7, "x_center_img.png")
        
        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_1.get_figure() == "X":
            self.triki_player1 = True
            self.triki(2, 5, 8, "x_center_img.png")

        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(2, 4, 6, "x_right_img.png")

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[1].image_src == "X_img.png" and self.list_containers[2].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(0, 1, 2, "x_hor_img.png")

        elif self.list_containers[3].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(3, 4, 5, "x_hor_img.png")

        elif self.list_containers[6].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_1.get_figure() == "X":

            self.triki_player1 = True
            self.triki(6, 7, 8, "x_hor_img.png")
        
        # player 1 con la o

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(0, 4, 8, "o_left_img.png")
            

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[3].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(0, 3, 6, "o_center_img.png")
        
        elif self.list_containers[1].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(1, 4, 7, "o_center_img.png")
        
        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(2, 5, 8, "o_center_img.png")

        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(2, 4, 6, "o_right_img.png")

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[1].image_src == "O_img.png" and self.list_containers[2].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(0, 1, 2, "o_hor_img.png")

        elif self.list_containers[3].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(3, 4, 5, "o_hor_img.png")

        elif self.list_containers[6].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_1.get_figure() == "O":

            self.triki_player1 = True
            self.triki(6, 7, 8, "o_hor_img.png")

        # player 2 con la o
        
        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(0, 4, 8, "o_left_img.png")

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[3].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(0, 3, 6, "o_center_img.png")
        
        elif self.list_containers[1].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(1, 4, 7, "o_center_img.png")
        
        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(2, 5, 8, "o_center_img.png")

        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(2, 4, 6, "o_right_img.png")

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[1].image_src == "O_img.png" and self.list_containers[2].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(0, 1, 2, "o_hor_img.png")

        elif self.list_containers[3].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(3, 4, 5, "o_hor_img.png")

        elif self.list_containers[6].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png" and self.player_2.get_figure() == "O":

            self.triki_player2 = True
            self.triki(6, 7, 8, "o_hor_img.png")

        # player 2 con la x 

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(0, 4, 8, "x_left_img.png")

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[3].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(0, 3, 6, "x_center_img.png")
        
        elif self.list_containers[1].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(1, 4, 7, "x_center_img.png")
        
        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(2, 5, 8, "x_center_img.png")

        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(2, 4, 6, "x_right_img.png")

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[1].image_src == "X_img.png" and self.list_containers[2].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(0, 1, 2, "x_hor_img.png")

        elif self.list_containers[3].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(3, 4, 5, "x_hor_img.png")

        elif self.list_containers[6].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png" and self.player_2.get_figure() == "X":

            self.triki_player2 = True
            self.triki(6, 7, 8, "x_hor_img.png")
        else:
            no_win = False
            contador = 0
            for n in self.list_containers:
                if n.image_src:
                    contador += 1
            
            if contador == 9:
                self.clean_table()

    # funcion para iniciar el juego
    def check_star(self, e):

        if self.playing and self.figure_P1.value and self.figure_P2.value:

            for i in self.list_containers:

                if i.image_src and i.data[1]:
                    i.image_src = ""
                    i.data[1] = False
                    time.sleep(0.090)
                    self.page.update()
        
            self.triki_player1 = False
            self.triki_player2 = False

            self.click_start = True
            self.audio_start_game.play()
            self.playing = False

            self.container_player_1.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="#3bcc4f",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
            self.container_player_2.shadow = BoxShadow(
                    spread_radius=7,
                    blur_radius=20,
                    color="",
                    offset=flet.Offset(0, 0),
                    blur_style=flet.ShadowBlurStyle.NORMAL,
                )
            self.page.update()
        elif not self.playing or self.figure_P1.value == "" or self.figure_P2.value == "":
            self.audio_error.play()

    # metodo para llamar la interfaz grafica
    def start(self):
        self.page.add(self.firstContainer)
        self.change_color_names()
        self.page.update()
        

# funcion para iniciar el programa
def inicio(page):
    app = Gui_app(page)
    app.start()
    page.update()

flet.app(target=inicio)