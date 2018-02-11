import unittest
from qualify import say_hello

# These example test cases are editable, feel free to add
# your own tests to debug your code.

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_say_hello(self):
    self.assertEqual(say_hello("Qualified"), "Hello, Qualified!")

myt = Test
myt.test_should_say_hello()