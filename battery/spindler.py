from .battery import Battery
from datetime import _Date

class Spindler(Battery):
    def __init__(self, last_service_date: _Date, current_date: _Date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date
