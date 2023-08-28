from .car import Car
from battery import Spindler, Nubbin
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from tires import Carrigan, Octoprime
from datetime import date

class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        wear_sensor_data: list[float]
    ) -> Car:

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = Carrigan(wear_sensor_data)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        wear_sensor_data: list[float]
    ) -> Car:

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = Octoprime(wear_sensor_data)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date,
        warning_light_is_on: bool,
        wear_sensor_data: list[float]
    ) -> Car:

        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(last_service_date, current_date)
        tires = Carrigan(wear_sensor_data)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        wear_sensor_data: list[float]
    ) -> Car:

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = Octoprime(wear_sensor_data)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        wear_sensor_data: list[float]
    ) -> Car:

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = Carrigan(wear_sensor_data)
        return Car(engine, battery, tires)
