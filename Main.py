import flet

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
    BoxShadow
)


class Gui_app:

    def __init__(self, page):

        self.page = page

        self.page.window.width = 680
        self.page.window.height = 550

        self.page.window.center()
        # self.page.update()

        self.text_user_1 = Row(
            controls=[
                Text("Jugador 1")
                ],alignment=flet.MainAxisAlignment.CENTER
            )
        self.text_user_2 = Row(
            controls=[
                Text("Jugador 2")
                ],alignment=flet.MainAxisAlignment.CENTER
            )

        self.container_1 = Container(
            margin=flet.margin.only(top=0, bottom=-8, right=-5),
            bgcolor="red",
            width=100,
            height=100,
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
            margin=flet.margin.only(top=0, bottom=-8, right=-5),
            bgcolor="red",
            width=100,
            height=100,
            border_radius=10,
            ink=True,
            on_click=lambda e: print("-- seleccionado"),
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
           margin=flet.margin.only(top=0, bottom=-8, right=-5),
            bgcolor="red",
            width=100,
            height=100,
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
            margin=flet.margin.only(top=0, bottom=-8, right=-5),
            bgcolor="red",
            width=100,
            height=100,
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
            margin=flet.margin.only(top=0, bottom=0, right=-5),
            bgcolor="red",
            width=100,
            height=100,
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
            margin=flet.margin.only(top=0, bottom=0, right=-5),
            bgcolor="red",
            width=100,
            height=100,
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
            bgcolor="red",
            content=self.text_user_1,
            width=150,
            height=30,
            border_radius=10,
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=30,
                color=flet.colors.BLUE_GREY_300,
                offset=flet.Offset(0, 0),
                blur_style=flet.ShadowBlurStyle.OUTER,
            )
        )

        self.container_player_2 = Container(
            bgcolor="red",
            content=self.text_user_2,
            width=150,
            height=30,
            border_radius=10,
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=30,
                color=flet.colors.BLUE_GREY_300,
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

        self.container = Container(
            bgcolor="transparent",
            expand=True,
            margin=-10,
            height=self.page.height,
            content=Column(
                controls=[
                    self.row_data,
                    self.row_1,
                    self.row_2,
                    self.row_3,
                ],
                alignment=flet.MainAxisAlignment.CENTER
            )
        )
        
        self.firstContainer = Container(
            bgcolor="green",
            image_src="bground.png",
            image_fit="FILL",
            content=self.container,
            expand=True,
            height=self.page.height,
            # width=self.page.width,
            margin=-10,
        )


    def start(self):
        self.page.add(self.firstContainer)


def inicio(page):
    app = Gui_app(page)
    app.start()
    page.update()

flet.app(target=inicio)