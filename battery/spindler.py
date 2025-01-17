from .battery import Battery
from datetime import date

class Spindler(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 3)
        return service_threshold_date < self._current_date
