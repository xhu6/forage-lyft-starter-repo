from .engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool) -> None:
        self._warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self._warning_light_is_on
