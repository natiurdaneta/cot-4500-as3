import unittest
from src.main.assignment_3 import euler_method, runge_kutta_method

class TestAssignment3(unittest.TestCase):
    def test_euler_method(self):
        def f(t, y):
            return t - y**2
        result = euler_method(f, (0, 2), 1, 10)
        self.assertAlmostEqual(result, 1.2446380979332121, places=10)

    def test_runge_kutta_method(self):
        def f(t, y):
            return t - y**2
        result = runge_kutta_method(f, (0, 2), 1, 10)
        self.assertAlmostEqual(result, 1.251316587879806, places=10)

if __name__ == "__main__":
    unittest.main()
