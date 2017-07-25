from unittest import TestCase, skip

from elevator.main import Elevator
from elevator.errors import FloorError

class TestElevator(TestCase):
    def setUp(self):
        self.elevator = Elevator(15)

    def test_elevator_comes_to_correct_floor(self):
        self.assertEqual(self.elevator.call_elevator(calling_floor=5), 5)

    def test_elevator_goes_to_correct_floor(self):
        self.assertEqual(self.elevator.go_to_floor(destination_floor=6), 6)

    def test_error_thrown_on_invalid_floor(self):
        with self.assertRaises(FloorError):
            self.elevator.go_to_floor(1776)
