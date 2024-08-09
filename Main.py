import flet
import time

from flet import (
    Container,
    Text,
    IconButton,
    Icon,
    Image,
    ImageFit,
    Column,
    Row,
    Alignment,
    LinearGradient,
    BoxShadow,
    FontWeight,
    AlertDialog,
    TextField,
    ElevatedButton,
    Checkbox,
    TextButton,
    Audio
)

class Player:

    def __init__(self):

        self.name = ""
        self.shift = False
        self.game_won = 0
        self.figure = ""
        
    def get_shift(self):
        return self.shift
    
    def set_shitf(self, shift):
        self.shift = shift

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_game_won(self):
        return self.game_won
    
    def set_game_won(self, num):
        self.game_won = num

    def get_figure(self):
        return self.figure
    
    def set_figure(self, figure):
        self.figure = figure

    def get_info_player(self, jugador):
        print(f"- {jugador}\n   - Nombre: {self.name}\n   - turno: {self.shift}\n   - juegos ganados: {self.game_won}\n   - figura: {self.figure}")

    

class Gui_app:

    def __init__(self, page):

        self.page = page
        
        self.num_clean_widgets = 0
        self.playing = False
        self.click_start = False
        self.triki_player1 = False
        self.triki_player2 = False

        self.player_1 = Player()
        self.player_2 = Player()

        self.player_1.set_shitf(True)
        self.player_2.set_shitf(False)

        self.page.window.height = 520
        self.page.window.width = 680

        self.page.window.max_width = 680
        self.page.window.max_height = 520

        self.page.window.min_width = 680
        self.page.window.min_height = 520

        self.page.window.center()
        # self.page.update()

        self.edit_name = 0
        self.games_num = Text(
            "0",
            weight=FontWeight.W_500,
            color="white"
        )

        self.games_count = Text(
            "0",
            weight=FontWeight.W_500,
            color="white"
        )

        self.text_of = Text(
            "of",
            weight=FontWeight.W_500,
            color="white"
        )

        self.text_player_1 = Text(
                        "Player 1", 
                        weight=FontWeight.W_700
                    )
        
        self.text_player_2 = Text(
                        "Player 2",
                        weight=FontWeight.W_700
                    )
        
        self.games_won_P1 = Text(
            "0",
            weight=FontWeight.W_500
        )

        self.games_won_P2 = Text(
            "0",
            weight=FontWeight.W_500
        )

        self.figure_P1 = Text(
            "",
            weight=FontWeight.W_700,
            size=20
        )

        self.figure_P2 = Text(
            "",
            weight=FontWeight.W_700,
            size=20
        )

        self.row_player_1 = Row(
            controls=[
                self.figure_P1,
                self.text_player_1,
                self.games_won_P1,
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )
        self.row_player_2 = Row(
            controls=[
                self.figure_P2,
                self.text_player_2,
                self.games_won_P2
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )

        self.container_1 = Container(
            margin=flet.margin.only(top=0, bottom=-4, right=-4),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=1,
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
            image_fit="FILL",
            width=100,
            height=100,
            border_radius=10,
            ink=True,
            data=2,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=3,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=4,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=5,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=6,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=7,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=8,
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
            image_fit="FILL",
            border_radius=10,
            ink=True,
            data=9,
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

        self.container_player_2 = Container(
            bgcolor="#f4faf5",
            content=self.row_player_2,
            width=150,
            height=30,
            on_click=lambda e: self.open_dialog(e.control.data),
            border_radius=10,
            data='2',
        )

        self.row_data = Row(
            controls=[
                self.container_player_1,
                self.container_player_2
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

        self.container_play = Container(
            bgcolor="#26994e",
            width=90,
            height=28,
            border_radius=10,
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

        self.row_container_play = Row(
            spacing=20,
            controls=[
                Column(width=70),
                self.container_num_games,
                self.container_play
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )

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

        self.column_all = Column(
            spacing=10,
            controls=[
                self.row_data,
                self.row_container_play,
                self.container_all,
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )
        
        self.firstContainer = Container(
            bgcolor="green",
            image_src="bground.png",
            image_fit="FILL",
            content=self.column_all,
            expand=True,
            ink=True,
            on_click=lambda e: print("- seleccionado"),
            height=self.page.height,
            # width=self.page.width,
            margin=-10,
        )

        self.input_name_p1 = TextField(
            width=180,
            label="Name player 1",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        self.input_num_game = TextField(
            width=50,
            #height=25,
            label="N°",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        self.input_name_p2 = TextField(
            width=230,
            label="Name player 2",
            border_radius=10,
            autofocus=True,
            border_color="white"
        )

        self.check_x_p1 = Checkbox(
            label="X",
            active_color="#095b2d"
        )

        self.check_o_p1 = Checkbox(
            label="O",
            active_color="#095b2d"
        )

        self.check_x_p2 = Checkbox(
            label="X",
            active_color="#095b2d"
        )

        self.check_o_p2 = Checkbox(
            label="O",
            active_color="#095b2d"
        )

        self.dialog_names_p1 = AlertDialog(
            modal=True,
            bgcolor="#a7c2ad",
            title=Text("Welcome", weight=FontWeight.W_700),
            actions=[]
        )

        self.dialog_names_p2 = AlertDialog(
            modal=True,
            bgcolor="#a7c2ad",
            title=Text("Welcome", weight=FontWeight.W_700),
        )

        self.button_check = IconButton(
                                    icon="CHECK_CIRCLE_ROUNDED",
                                    icon_color="#095b2d",
                                    icon_size=30,
                                    on_click=self.close_dialog
                                    )
        
        self.button_clean = IconButton(
                                    icon="DELETE_SWEEP_ROUNDED",
                                    icon_color="#da132c",
                                    icon_size=30,
                                    on_click=self.clean_widgets_info
                                    )

        self.list_containers = [
            self.container_1, self.container_2, self.container_3,
            self.container_4, self.container_5, self.container_6,
            self.container_7, self.container_8, self.container_9
        ]

        self.auido_star = Audio(
            src="assets/start_game.wav",
            autoplay=True,
            volume=1
        )

        self.auido_click_container = Audio(
            src="assets/click_container.wav",
            autoplay=True
        )
        

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
            self.page.update()

        elif self.num_clean_widgets == 2:

            self.figure_P2.value = ""
            self.figure_P1.value = ""
            self.input_name_p1.value = ""
            self.check_x_p2.disabled = False
            self.check_x_p2.value = False
            self.check_o_p2.disabled = False
            self.check_o_p2.value = False

            self.check_x_p1.disabled = False
            self.check_x_p1.value = False
            self.check_o_p1.disabled = False
            self.check_o_p1.value = False
            self.page.update()

    def open_dialog(self, e):
        if e == '1':
            # print(f"num action -> {len(self.dialog_names_p1.actions)}")
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

    def close_dialog(self, e):

        if self.input_name_p1.value and self.input_name_p2.value and self.input_num_game.value:
            self.container_play.shadow = BoxShadow(
                                                spread_radius=7,
                                                blur_radius=20,
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
                print(self.games_num, self.input_num_game.value)
                self.page.update()

            elif not self.check_o_p1.value and not self.check_x_p1.value:
                print(self.dialog_names_p1.actions)

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

                self.player_2.set_name(self.input_name_p1.value)
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
                    print("-- no numero no nombre")
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
                    print("-- si nombre pero no nuemero")
                    for i in range(1, 6):

                        self.input_num_game.border_color = flet.colors.ERROR
                        self.page.update()
                        time.sleep(0.1)
                        self.input_num_game.border_color = "white"
                        self.page.update()
                        time.sleep(0.1)

                elif not self.input_name_p1.value and self.input_num_game.value:
                    print("-- no nombre si numero")
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

    def triki(self, num1, num2, num3, image):
        print(type(num1), type(num2), type(num3), type(image))
        self.list_containers[int(num1)].image_src = image
        self.list_containers[int(num2)].image_src = image
        self.list_containers[int(num3)].image_src = image
        self.page.update()

    def player_win(self):
        pass


    def play(self, e):

        if self.text_player_1.value != "Player 1" and self.text_player_2.value != "Player 2" and self.click_start:
            print("-- puede iniciar e juego")
            # print(f"-- Turno player 1 {self.player_1.get_shift()}")
            if self.player_1.get_shift() and not self.player_2.get_shift():
                print(f"turno de player 1: {self.player_1.get_shift()}")
                print(f"figura: {self.player_1.get_figure()}")
                for i in self.list_containers:
                    if i.data == e and i.image_src == None and self.player_1.get_figure() == "X":
                        print(f"data de i: {i.data}, {e} - src {i.image_src}")
                        i.image_src = "X_img.png"
                        # self.page.update()
                        self.page.overlay.append(self.auido_click_container)
                        self.page.update()
                        self.auido_click_container.play()
                        self.page.update()
                        print(f"src: {i.image_src}")
                    elif i.data == e and i.image_src == None and self.player_1.get_figure() == "O":
                        print(f"data de i: {i.data}, {e} - src {i.image_src}")
                        i.image_src = "O_img.png"
                        # self.page.update()
                        self.page.overlay.append(self.auido_click_container)
                        self.page.update()
                        self.auido_click_container.play()
                        self.page.update()
                        print(f"src: {i.image_src}")
                self.player_1.set_shitf(False)
                self.player_2.set_shitf(True)

                print(f"turno de 1 {self.player_1.get_shift()}")
                print(f"turno de 2 {self.player_2.get_shift()}")

            elif self.player_2.get_shift() and not self.player_1.get_shift():

                print(f"turno de player 2: {self.player_2.get_shift()}")
                for j in self.list_containers:
                    if j.data == e and j.image_src == None and self.player_2.get_figure() == "X":
                        print(f"data de i: {j.data}, {e} - src {j.image_src}")
                        j.image_src = "X_img.png"
                        # self.page.update()
                        self.page.overlay.append(self.auido_click_container)
                        self.page.update()
                        self.auido_click_container.play()
                        self.page.update()
                    elif j.data == e and j.image_src == None and self.player_2.get_figure() == "O":
                        print(f"data de i: {j.data}, {e} - src {j.image_src}")
                        j.image_src = "O_img.png"
                        # self.page.update()
                        self.page.overlay.append(self.auido_click_container)
                        self.page.update()
                        self.auido_click_container.play()
                        self.page.update()
                self.player_1.set_shitf(True)
                self.player_2.set_shitf(False)

        # change img of X
        
        if self.list_containers[0].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png":

            self.triki(0, 4, 8, "x_left_img.png")
            self.triki_player1 = True

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[3].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png":

            self.triki(0, 3, 6, "x_center_img.png")
            self.triki_player1 = True
        
        elif self.list_containers[1].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png":

            self.triki(1, 4, 7, "x_center_img.png")
            self.triki_player1 = True
        
        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png":

            self.triki(2, 5, 8, "x_center_img.png")
            self.triki_player1 = True

        elif self.list_containers[2].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[6].image_src == "X_img.png":

            self.triki(2, 4, 6, "x_right_img.png")
            self.triki_player1 = True

        elif self.list_containers[0].image_src == "X_img.png" and self.list_containers[1].image_src == "X_img.png" and self.list_containers[2].image_src == "X_img.png":

            self.triki(0, 1, 2, "x_hor_img.png")
            self.triki_player1 = True

        elif self.list_containers[3].image_src == "X_img.png" and self.list_containers[4].image_src == "X_img.png" and self.list_containers[5].image_src == "X_img.png":

            self.triki(3, 4, 5, "x_hor_img.png")
            self.triki_player1 = True

        elif self.list_containers[6].image_src == "X_img.png" and self.list_containers[7].image_src == "X_img.png" and self.list_containers[8].image_src == "X_img.png":

            self.triki(6, 7, 8, "x_hor_img.png")
            self.triki_player1 = True

        # change img of O
        
        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png":

            self.triki(0, 4, 8, "o_left_img.png")
            self.triki_player2 = True

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[3].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png":

            self.triki(0, 3, 6, "o_center_img.png")
            self.triki_player2 = True
        
        elif self.list_containers[1].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png":

            self.triki(1, 4, 7, "o_center_img.png")
            self.triki_player2 = True
        
        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png":

            self.triki(2, 5, 8, "o_center_img.png")
            self.triki_player2 = True

        elif self.list_containers[2].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[6].image_src == "O_img.png":

            self.triki(2, 4, 6, "o_right_img.png")
            self.triki_player2 = True

        elif self.list_containers[0].image_src == "O_img.png" and self.list_containers[1].image_src == "O_img.png" and self.list_containers[2].image_src == "O_img.png":

            self.triki(0, 1, 2, "o_hor_img.png")
            self.triki_player2 = True

        elif self.list_containers[3].image_src == "O_img.png" and self.list_containers[4].image_src == "O_img.png" and self.list_containers[5].image_src == "O_img.png":

            self.triki(3, 4, 5, "o_hor_img.png")
            self.triki_player2 = True

        elif self.list_containers[6].image_src == "O_img.png" and self.list_containers[7].image_src == "O_img.png" and self.list_containers[8].image_src == "O_img.png":

            self.triki(6, 7, 8, "o_hor_img.png")
            self.triki_player2 = True
    

    def check_star(self, e):
        self.click_start = True

        audio_error = Audio(
            src="assets/error_start.wav",
            autoplay=True
        )

        if self.playing:

            self.page.overlay.append(self.auido_star)
            self.page.update()
            print("-- Reproduciendo")
            self.auido_star.play()
            print("-- saliendo de reproduccion")
            self.page.update()
            self.playing = False
        elif not self.playing:
            self.page.overlay.append(audio_error)
            self.page.update()
            audio_error.play()
            self.page.update()

    def change_x(self, e):
        print("x 2 seleccionada")
        self.container_2.image_src = "assets/O_img.png"
        self.page.update()

    def start(self):

        self.page.add(self.firstContainer)
        self.change_color_names()
        self.page.update()


def inicio(page):
    app = Gui_app(page)
    app.start()
    page.update()

flet.app(target=inicio)