from .serviceable import Serviceable
from battery import Battery
from engine import Engine

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        return self._battery.needs_service() or self._engine.needs_service()
