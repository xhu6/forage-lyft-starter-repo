from .car import Car
from battery import Spindler, Nubbin
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from datetime import _Date

class CarFactory:
    @staticmethod
    def create_calliope(current_date: _Date, last_service_date: _Date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: _Date, last_service_date: _Date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: _Date, last_service_date: _Date, warning_light_is_on: bool) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: _Date, last_service_date: _Date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: _Date, last_service_date: _Date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)
