import unittest
from calculator import *

class TestCalculate(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_operators(self):
    self.assertEqual(calculate("add", self.x, self.y), 6)
    self.assertEqual(calculate("substract", self.x, self.y), 2)
    self.assertEqual(calculate("multiply", self.x, self.y), 8)
    self.assertEqual(calculate("divide", self.x, self.y), 2)
    self.assertEqual(calculate("power", self.x, self.y), 16)
    self.assertEqual(calculate("square_root", self.x, self.y), 2)

  def test_wrong_operator(self):
    with self.assertRaises(UnboundLocalError):
      calculate("", self.x, self.y)
  
  def test_too_many_parameters(self):
    with self.assertRaises(TypeError):
      calculate("add", self.x, self.y, 42)


class TestAddMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_add(self):
    self.assertEqual(Calculator.add(self.x, self.y), 6)

  def test_add_wrong_x_type(self):
    with self.assertRaises(TypeError):
      Calculator.add("4", self.y)
  
  def test_add_wrong_y_type(self):
    with self.assertRaises(TypeError):
      Calculator.add(self.x, "2")

  def test_add_string_parameters(self):
    self.assertEqual(Calculator.add("4", "2"), "42")

class TestSubtractMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_subtract(self):
    self.assertEqual(Calculator.subtract(self.x, self.y), 2)

  def test_subtract_wrong_x_type(self):
    with self.assertRaises(TypeError):
      Calculator.subtract("4", self.y)
  
  def test_subtract_wrong_y_type(self):
    with self.assertRaises(TypeError):
      Calculator.subtract(self.x, "2")

class TestMultiplyMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_multiply(self):
    self.assertEqual(Calculator.multiply(self.x, self.y), 8)

  def test_multiply_wrong_x_type(self):
    self.assertEqual(Calculator.multiply("4", self.y), "44")
  
  def test_multiply_wrong_y_type(self):
    self.assertEqual(Calculator.multiply(self.x, "2"), "2222")

  def test_multiply_string_parameters(self):
    with self.assertRaises(TypeError):
      Calculator.multiply("4", "2")

class TestDivideMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_divide(self):
    self.assertEqual(Calculator.divide(self.x, self.y), 2)

  def test_divide_wrong_x_type(self):
    with self.assertRaises(TypeError):
      Calculator.divide("4", self.y)
  
  def test_divide_wrong_y_type(self):
    with self.assertRaises(TypeError):
      Calculator.divide(self.x, "2")

class TestPowerMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4
    self.y = 2

  def test_power(self):
    self.assertEqual(Calculator.power(self.x, self.y), 16)

  def test_power_wrong_x_type(self):
    with self.asserRaise(TypeError):
      Calculator.power("4", self.y)
  
  def test_power_wrong_y_type(self):
    with self.asserRaise(TypeError):
      Calculator.power(self.x, "2")

class TestSquareRootMethod(unittest.TestCase):
  def __init__(self):
    self.x = 4

  def test_square_root(self):
    self.assertEqual(Calculator.square_root(self.x), 2)

  def test_square_root_wrong_x_type(self):
    with self.assertRaises(TypeError):
      Calculator.square_root("4")


if __name__ == '__main__':
    unittest.main()