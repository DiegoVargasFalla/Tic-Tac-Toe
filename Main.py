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
)


class Gui_app:

    def __init__(self, page):

        self.page = page

        self.page.window.width = 680
        self.page.window.height = 550

        self.page.window.center()
        # self.page.update()

        self.container_1 = Container(
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