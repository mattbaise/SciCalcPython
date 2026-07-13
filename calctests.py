import importlib.util
import pathlib
import unittest

from calculator import Calculator


spec = importlib.util.spec_from_file_location("main_app", pathlib.Path(__file__).with_name("main-app.py"))
main_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_app)


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
    
    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(90, 45), 45)
    
    def test_sub3(self):
        c = Calculator()
        self.assertEqual(c.sub(100, 89), 11)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.multiply(3, 3), 9)

    def test_normalize_operation(self):
        self.assertEqual(main_app.normalize_operation(" Multiply "), "multiply")
        self.assertEqual(main_app.normalize_operation("+"), "add")
        self.assertEqual(main_app.normalize_operation("SQRT"), "squareRoot")


    def test_toggle_mode(self):
        self.assertEqual(main_app.toggle_mode("basic"), "scientific")
        self.assertEqual(main_app.toggle_mode("scientific"), "basic")

    def test_set_mode(self):
        self.assertEqual(main_app.set_mode("basic", "scientific"), "scientific")
        self.assertEqual(main_app.set_mode("scientific", "basic"), "basic")
        self.assertEqual(main_app.set_mode("basic", "unknown"), "basic")

    def test_set_angle_mode(self):
        self.assertEqual(main_app.set_angle_mode("degrees", "radians"), "radians")
        self.assertEqual(main_app.set_angle_mode("radians", "degrees"), "degrees")
        self.assertEqual(main_app.set_angle_mode("degrees", "unknown"), "degrees")

    def test_multiply2(self):
        c = Calculator()
        self.assertEqual(c.multiply(12, 10), 120)

    def test_multiply3(self):
        c = Calculator()
        self.assertEqual(c.multiply(5, 8), 40)  
    
    def test_division(self):
        c = Calculator()
        self.assertEqual(c.division(9, 3), 3)

    def test_division2(self):
        c = Calculator()
        self.assertEqual(c.division(90, 45), 2)

    def test_division3(self):
        c = Calculator()
        self.assertEqual(c.division(100, 10), 10)
    
    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3), 9)
    
    def test_square2(self):
        c = Calculator()
        self.assertEqual(c.square(12), 144)

    def test_square3(self):
        c = Calculator()
        self.assertEqual(c.square(5), 25)
    
    def test_squareRoot(self):
        c = Calculator()
        self.assertEqual(c.squareRoot(9), 3)
    
    def test_squareRoot2(self):
        c = Calculator()
        self.assertEqual(c.squareRoot(144), 12)

    def test_squareRoot3(self):
        c = Calculator()
        self.assertEqual(c.squareRoot(25), 5)
    
    def test_variableExponent(self):
        c = Calculator()
        self.assertEqual(c.variableExponent(2, 3), 8)
    
    def test_variableExponent2(self):
        c = Calculator()
        self.assertEqual(c.variableExponent(5, 2), 25)

    def test_variableExponent3(self):
        c = Calculator()
        self.assertEqual(c.variableExponent(3, 4), 81)
    
    def test_sin(self):
        c = Calculator()
        self.assertAlmostEqual(c.sin(0), 0.0)
    
    def test_sin2(self):
        c = Calculator()
        self.assertAlmostEqual(c.sin(3.14159 / 2), 1.0)
    
    def test_sin3(self):
        c = Calculator()
        self.assertAlmostEqual(c.sin(3.14159), 0.0)
    
    def test_cos(self):
        c = Calculator()
        self.assertAlmostEqual(c.cos(0), 1.0)
    
    def test_cos2(self):
        c = Calculator()
        self.assertAlmostEqual(c.cos(3.14159 / 2), 0.0)
    
    def test_cos3(self):
        c = Calculator()
        self.assertAlmostEqual(c.cos(3.14159), -1.0)
    
    def test_tan(self):
        c = Calculator()
        self.assertAlmostEqual(c.tan(0), 0.0)
    
    def test_tan2(self):
        c = Calculator()
        self.assertAlmostEqual(c.tan(3.14159 / 4), 1.0)
    
    def test_tan3(self):
        c = Calculator()
        self.assertAlmostEqual(c.tan(3.14159 / 2), 0.0, places=5)  # tan(pi/2) is undefined, but we can test for a large value.
    
    def test_inverseSin(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseSin(0), 0.0)
    
    def test_inverseSin2(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseSin(1), 3.14159 / 2, places=5)

    def test_inverseSin3(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseSin(-1), -3.14159 / 2, places=5)
    
    def test_inverseCos(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseCos(1), 0.0)
    
    def test_inverseCos2(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseCos(0), 3.14159 / 2, places=5)
    
    def test_inverseCos3(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseCos(-1), 3.14159, places=5)
    
    def test_inverseTan(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseTan(0), 0.0)
    
    def test_inverseTan2(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseTan(1), 3.14159 / 4, places=5)
    
    def test_inverseTan3(self):
        c = Calculator()
        self.assertAlmostEqual(c.inverseTan(-1), -3.14159 / 4, places=5)

    def test_factorial(self):
        c = Calculator()
        self.assertEqual(c.factorial(5), 120)

    def test_factorial2(self):
        c = Calculator()
        self.assertEqual(c.factorial(0), 1)
    
    def test_factorial3(self):
        c = Calculator()
        self.assertEqual(c.factorial(3), 6)
        
    



if __name__ == '__main__':
    unittest.main()
