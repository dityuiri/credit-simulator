from models.constants import VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, VEHICLE_CONDITION_OLD, BASE_INTEREST_RATE_CAR
from models.credits import Vehicle, Credit

import unittest


class TestVehicle(unittest.TestCase):
    def test_valid_vehicle(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        self.assertEqual(vehicle.vehicle_type, VEHICLE_TYPE_CAR)
        self.assertEqual(vehicle.condition, VEHICLE_CONDITION_NEW)
        self.assertEqual(vehicle.year, 2023)

    def test_invalid_vehicle(self):
        # Test invalid vehicle creation
        with self.assertRaises(ValueError):
            Vehicle("InvalidType", VEHICLE_CONDITION_NEW, 2023)

        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, "InvalidCondition", 2023)

        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 100)

    def test_new_vehicle_condition(self):
        # Test condition-specific validation
        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2070)

    def test_old_vehicle_condition(self):
        # Test condition-specific validation
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_OLD, 2020)
        self.assertEqual(vehicle.vehicle_type, VEHICLE_TYPE_CAR)
        self.assertEqual(vehicle.condition, VEHICLE_CONDITION_OLD)
        self.assertEqual(vehicle.year, 2020)


class TestCredit(unittest.TestCase):
    def test_valid_credit(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        credit = Credit(vehicle, 20000, 8000, 36)
        self.assertEqual(credit.total_credit, 20000)
        self.assertEqual(credit.down_payment, 8000)
        self.assertEqual(credit.tenure, 36)

    def test_invalid_credit(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)

        with self.assertRaises(ValueError):
            Credit(vehicle, 25000, 4000, 6)  # Invalid tenure

        with self.assertRaises(ValueError):
            Credit(vehicle, 25000, -1000, 36)  # Negative down payment

        with self.assertRaises(ValueError):
            Credit(vehicle, 25000, 4000, 36)  # Insufficient down payment for new vehicle

    def test_interest_rate(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        credit = Credit(vehicle, 20000, 8000, 36)
        self.assertEqual(credit.base_interest_rate, BASE_INTEREST_RATE_CAR)


if __name__ == '__main__':
    unittest.main()
