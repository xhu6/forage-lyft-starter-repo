import unittest
from tires import Carrigan, Octoprime

class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        tires = Carrigan([0.0000, 0.2502, 0.8451, 0.9000])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self) -> None:
        tires = Carrigan([0.8998, 0.8344, 0.8451, 0.8999])
        self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self) -> None:
        tires = Octoprime([0.3001, 0.9, 0.9, 0.9])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self) -> None:
        tires = Octoprime([0.2999, 0.9, 0.9, 0.9])
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()
