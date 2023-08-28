from .engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > 30000
