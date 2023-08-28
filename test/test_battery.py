import unittest
from datetime import datetime
from battery import Spindler, Nubbin

class TestSpindler(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = Spindler(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self) -> None:
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = Spindler(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = Nubbin(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self) -> None:
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = Nubbin(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == "__main__":
    unittest.main()
