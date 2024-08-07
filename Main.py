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
    Checkbox
)

class Player:

    def __init__(self):

        self.name = ""
        self.shift = False
        self.game_won = 0
        pass

class Gui_app:

    def __init__(self, page):

        self.page = page

        self.page.window.height = 520
        self.page.window.width = 680

        self.page.window_max_width = 680
        self.page.window_max_height = 520

        self.page.window_min_width = 680
        self.page.window_min_height = 520

        self.page.window.center()
        # self.page.update()

        self.edit_name = 0

        self.text_player_1 = Text(
                        "Player 1", 
                        weight=FontWeight.W_600
                    )
        
        self.text_player_2 = Text(
                        "Player 2",
                        weight=FontWeight.W_600
                    )
        
        self.games_won_P1 = Text(
            "0",
            weight=FontWeight.W_600
        )

        self.games_won_P2 = Text(
            "0",
            weight=FontWeight.W_600
        )

        self.row_player_1 = Row(
            controls=[
                self.text_player_1,
                self.games_won_P1,
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )
        self.row_player_2 = Row(
            controls=[
                self.text_player_2,
                self.games_won_P2
                ],alignment=flet.MainAxisAlignment.SPACE_AROUND
            )

        self.container_1 = Container(
            margin=flet.margin.only(top=0, bottom=-8, right=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_2 = Container(
            margin=flet.margin.only(top=0, bottom=-8, right=-8),
            bgcolor="red",
            image_fit="FILL",
            width=100,
            height=100,
            border_radius=10,
            ink=True,
            on_click=self.change_x,
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_3 = Container(
            margin=flet.margin.only(top=0, bottom=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )
        

        self.container_4 = Container(
           margin=flet.margin.only(top=0, bottom=-8, right=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_5 = Container(
            margin=flet.margin.only(top=0, bottom=-8, right=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_6 = Container(
            margin=flet.margin.only(top=0, bottom=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_7 = Container(
            margin=flet.margin.only(top=0, bottom=0, right=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
            )
        )

        self.container_8 = Container(
            margin=flet.margin.only(top=0, bottom=0, right=-8),
            bgcolor="red",
            width=100,
            height=100,
            image_fit="FILL",
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
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
            on_click=lambda e: print("-- seleccionado"),
            gradient=flet.LinearGradient(
                begin=flet.alignment.top_center,
                end=flet.alignment.bottom_center,
                colors=["#2876bf", "#164f84", "#0c2d4d"],
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
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=30,
                color="#ce38ca",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.OUTER,
            )
        )

        self.container_player_2 = Container(
            bgcolor="#f4faf5",
            content=self.row_player_2,
            width=150,
            height=30,
            on_click=lambda e: self.open_dialog(e.control.data),
            border_radius=10,
            data='2',
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=30,
                color="#ce38ca",
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.OUTER,
            )
        )

        self.row_data = Row(
            controls=[
                self.container_player_1,
                self.container_player_2
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
            spacing=25,
            controls=[
                 self.row_data,
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
            height=self.page.height,
            # width=self.page.width,
            margin=-10,
        )

        self.input_name_p1 = TextField(
            label="Name player 1",
            border_radius=10,
            autofocus=True,
        )

        self.input_name_p2 = TextField(
            label="Name player 2",
            border_radius=10,
            autofocus=True,
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
            bgcolor="#9bb9a8",
            title=Text("Welcome", weight=FontWeight.W_700),
        )

        self.dialog_names_p2 = AlertDialog(
            modal=True,
            bgcolor="#9bb9a8",
            title=Text("Welcome", weight=FontWeight.W_700),
        )

        self.button_check = IconButton(
                                    icon="CHECK_CIRCLE_ROUNDED",
                                    icon_color="#095b2d",
                                    icon_size=30,
                                    on_click=self.close_dialog
                                    )

        self.list_containers = [
            [self.container_1], [self.container_2], [self.container_3],
            [self.container_4], [self.container_5], [self.container_6],
            [self.container_7], [self.container_2], [self.container_9]
        ]

    def open_dialog(self, e):
        if e == '1':
            print("-- primer contenedor", e)
            self.edit_name = 1
            self.dialog_names_p1.content = Container(
                                                bgcolor="transparent",
                                                height=50,
                                                ink=True,
                                                content=Column(
                                                    controls=[
                                                        self.input_name_p1,
                                                        ]
                                                    )
                                                )
            self.dialog_names_p1.actions = Row(
                                            controls=[
                                                    self.check_x_p1, 
                                                    self.check_o_p1,
                                                    self.button_check,
                                            ],
                                            alignment=flet.MainAxisAlignment.SPACE_AROUND
                                        ),
            self.page.overlay.append(self.dialog_names_p1)
            self.page.update()
            self.dialog_names_p1.open = True
            self.page.update()
            print("-- saliendo de pprimer contenedor")
        elif e == '2':
            print("-- segundo contenedor", e)
            self.edit_name = 2
            self.dialog_names_p2.content = Container(
                                                bgcolor="transparent",
                                                height=50,
                                                ink=True,
                                                content=Column(
                                                    controls=[
                                                        self.input_name_p2,
                                                        ]
                                                    )
                                                )
            self.dialog_names_p2.actions = Row(
                                            controls=[
                                                    self.check_x_p2, 
                                                    self.check_o_p2,
                                                    self.button_check,
                                            ],
                                            alignment=flet.MainAxisAlignment.SPACE_AROUND
                                        ),
            self.page.overlay.append(self.dialog_names_p2)
            self.page.update()
            self.dialog_names_p2.open = True
            self.page.update()

    def close_dialog(self, e):
        if self.edit_name == 1 and self.input_name_p1.value:
                self.page.update()
                print("-- edit = 1 y tiene texto el input")

                if self.check_x_p1.value and self.check_o_p1.value:
                    print("-- los dos check True")
                    for l in range(2):

                        self.check_o_p1.value = False
                        self.check_x_p1.value = False
                        self.page.update()
                        time.sleep(0.2)
                        self.check_o_p1.value = True
                        self.check_x_p1.value = True
                        self.page.update()
                        time.sleep(0.22)
                    
                    self.check_o_p1.value = False
                    self.check_x_p1.value = False
                    self.page.update()

                elif self.check_x_p1.value or self.check_o_p1.value:

                    print(self.check_o_p1.value, self.check_x_p1)
                    print(f"-- {self.edit_name, self.input_name_p1.value}")
                    self.text_player_1.value = self.input_name_p1.value.capitalize()
                    self.dialog_names_p1.open = False
                    self.dialog_names_p1.content = []
                    self.dialog_names_p1.actions = []
                    self.page.update()

                elif not self.check_o_p1.value and not self.check_x_p1.value:
                    print("ningun check es True")

                    for j in range(1, 5):

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
            print("-- edit = 2 y tiene valor en el input")

            if self.check_x_p2.value and self.check_o_p2.value:

                for l in range(2):
                    print("bucle")
                    self.check_o_p2.value = False
                    self.check_x_p2.value = False
                    self.page.update()
                    time.sleep(0.2)
                    self.check_o_p2.value = True
                    self.check_x_p2.value = True
                    self.page.update()
                    time.sleep(0.22)

                self.check_o_p2.value = False
                self.check_x_p2.value = False
                self.page.update()

            elif self.check_x_p2.value or self.check_o_p2.value:
                print("-- cerrando")
                self.text_player_2.value = self.input_name_p2.value.capitalize()
                self.dialog_names_p2.open = False
                self.dialog_names_p2.content = []
                self.dialog_names_p2.actions = []
                self.page.update()

            elif not self.check_x_p2.value and not self.check_o_p2.value:

                    for j in range(1, 5):
                        print("-- en el bulce")
                        self.check_o_p2.value = True
                        self.check_x_p2.value = True
                        self.page.update()
                        time.sleep(0.1)
                        self.check_o_p2.value = False
                        self.check_x_p2.value = False
                        self.page.update()
                        time.sleep(0.1)

        else:
            if not self.input_name_p1.value and self.edit_name == 1:
                print("input 1 no tiene texto y es igual a ", self.edit_name)
                for i in range(1, 7):
                    print("-- en el bulce de 1 ")
                    self.input_name_p1.border_color = flet.colors.ERROR
                    self.page.update()
                    time.sleep(0.1)
                    self.input_name_p1.border_color = "wihte"
                    self.page.update()
                    time.sleep(0.1)
                self.page.update()
            elif not self.input_name_p2.value and self.edit_name == 2:
                print("input 2 no tiene texto y es igual a ", self.edit_name)
                for j in range(1, 7):
                    print("-- en el bulce de 2 ")
                    self.input_name_p2.border_color = flet.colors.ERROR
                    self.page.update()
                    time.sleep(0.1)
                    self.input_name_p2.border_color = "wihte"
                    self.page.update()
                    time.sleep(0.1)
                self.page.update()

    def change_x(self, e):
        print("x 2 seleccionada")
        self.container_2.image_src = "O_img.png"
        self.page.update()

    def start(self):
        self.page.add(self.firstContainer)


def inicio(page):
    app = Gui_app(page)
    app.start()
    page.update()

flet.app(target=inicio)