import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_calculate_tip(self):
        c = Calculator()
        self.assertEqual(c.calculate_tip(80, 20, 2), (16.0, 96.0, 48.0))

    def test_fahrenheit_to_celsius(self):
        c = Calculator()
        self.assertEqual(c.fahrenheit_to_celsius(32), 0)

    def test_celsius_to_fahrenheit(self):
        c = Calculator()
        self.assertEqual(c.celsius_to_fahrenheit(100), 212)

    def test_memory_plus_and_recall(self):
        c = Calculator()
        c.state = 5
        c.M_plus()
        c.state = 10
        c.M_plus()

        self.assertEqual(c.memory, 15)
        self.assertEqual(c.MRC(), 15)

    def test_memory_clear(self):
        c = Calculator()
        c.memory = 12
        c.MC()

        self.assertEqual(c.memory, 0.0 )

    def test_switch_units_mode(self):
        c = Calculator()
        c.switchUnitsMode("rad")

        self.assertEqual(c.angle_mode, "RAD")
    

if __name__ == '__main__':
    unittest.main()
