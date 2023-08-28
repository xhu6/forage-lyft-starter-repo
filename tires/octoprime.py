from .tires import Tires

class Octoprime(Tires):
    def __init__(self, wear_sensor_data: list[float]) -> None:
        self._wear_sensor_data = wear_sensor_data

    def needs_service(self) -> bool:
        return sum(self._wear_sensor_data) >= 3
