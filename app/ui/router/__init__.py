from typing import Any, Awaitable, Callable, Dict, Union

from nicegui import background_tasks, ui
from nicegui.dependencies import register_component

register_component("router", __file__, "router.vue")


class Router:
    def __init__(self) -> None:
        """Router."""
        self.routes: Dict[str, Callable[[Any], Any]] = {}
        self.content: ui.element

    def add(self, path: str) -> Any:
        def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
            self.routes[path] = func
            return func

        return decorator

    def visit(self, target: Union[Callable[[Any], Any], str]) -> None:
        if isinstance(target, str):
            path = target
            builder = self.routes[target]
        else:
            path = {v: k for k, v in self.routes.items()}[target]
            builder = target

        async def build() -> None:
            with self.content:
                await ui.run_javascript(
                    f"""
                        if (window.location.pathname !== "{path}") {{
                            history.pushState({{page: "{path}"}}, "", "{path}")
                        }}
                    """,
                    respond=False,
                )

                result = builder()  # type: ignore[call-arg]

                if isinstance(result, Awaitable):
                    await result

        self.content.clear()
        background_tasks.create(build())

    def frame(self) -> ui.element:
        self.content = ui.element("router").on("open", lambda msg: self.visit(msg["args"]))  # type: ignore
        return self.content
