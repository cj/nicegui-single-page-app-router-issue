from nicegui import ui

from app.ui.router import Router


class Routes:
    def __init__(self) -> None:
        router = self.router = Router()

        @router.add("/")
        async def show_one():
            ui.label("Content One").classes("text-2xl")

        @router.add("/two")
        async def show_two():
            ui.label("Content Two").classes("text-2xl")

        @router.add("/three")
        async def show_three():
            ui.label("Content Three").classes("text-2xl")

        self.show_one = show_one
        self.show_two = show_two
        self.show_three = show_three
