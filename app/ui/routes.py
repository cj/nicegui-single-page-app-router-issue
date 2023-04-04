from nicegui import ui

from app.ui.router import Router

router = Router()


@router.add("/")
async def show_one():
    ui.label("Content One").classes("text-2xl")


@router.add("/two")
async def show_two():
    ui.label("Content Two").classes("text-2xl")


@router.add("/three")
async def show_three():
    ui.label("Content Three").classes("text-2xl")
