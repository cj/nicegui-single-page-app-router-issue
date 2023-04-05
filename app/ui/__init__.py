from fastapi import FastAPI
from nicegui import Client, ui

import app.ui.routes as Routes


def init(fastapi: FastAPI) -> None:
    @ui.page("/")  # normal index page (eg. the entry point of the app)
    @ui.page(
        "/{_:path}"
    )  # all other pages will be handled by the router but must be registered to also show the SPA index page
    async def main(client: Client) -> None:  # pyright: reportUnusedFunction=false
        routes = Routes.Routes()
        router = routes.router
        # adding some navigation buttons to switch between the different pages
        with ui.row():
            ui.button("One", on_click=lambda: router.visit(routes.show_one)).classes("w-32")
            ui.button("Two", on_click=lambda: router.visit(routes.show_two)).classes("w-32")
            ui.button("Three", on_click=lambda: router.visit(routes.show_three)).classes("w-32")

        # this places the content which should be displayed
        router.frame().classes("w-full p-4 bg-gray-100")

    ui.run_with(fastapi, title="NiceGUI")
