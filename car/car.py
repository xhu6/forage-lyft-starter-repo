from .serviceable import Serviceable
from battery import Battery
from engine import Engine
from tires import Tires

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        self._engine = engine
        self._battery = battery
        self._tires = tires

    def needs_service(self) -> bool:
        return self._battery.needs_service() \
            or self._engine.needs_service() \
            or self._tires.needs_service()
