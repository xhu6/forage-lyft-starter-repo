import unittest
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self) -> None:
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self) -> None:
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self) -> None:
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == "__main__":
    unittest.main()
