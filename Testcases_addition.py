import unittest

# import module which has to be tested
import Unit_Test_Addition


class TestAddition (unittest.TestCase):

    # All test function names should start with keyword 'test'

    def test_addition_one(self):

        # Arrange data so that variable values can be assigned at one place
        num1 = 10
        num2 = 5

        # Act
        result = Unit_Test_Addition.addition(num1, num2)

        # Assert
        self.assertEqual(result, num1+num2)

    def test_addition_two(self):

        # Arrange data so that variable values can be assigned at one place
        num1 = 3
        num2 = 'hello'

        # Act
        result = Unit_Test_Addition.addition(num1, num2)

        # Assert
        self.assertTrue(isinstance(result, ValueError))

    def test_addition_three(self):

        # Arrange data so that variable values can be assigned at one place
        num1 = None
        num2 = None

        # Act
        result = Unit_Test_Addition.addition(num1, num2)

        # Assert
        self.assertEqual(result, "Enter numbers")


unittest.main()
