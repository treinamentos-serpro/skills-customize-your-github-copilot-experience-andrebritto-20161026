import unittest


def is_passing(score):
    return score >= 60


def calculate_average(values):
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)


class TestCalculations(unittest.TestCase):
    def test_is_passing_at_threshold(self):
        self.fail("Replace this line with an assertion.")

    def test_is_passing_below_threshold(self):
        self.fail("Replace this line with an assertion.")

    def test_average_of_multiple_values(self):
        self.fail("Replace this line with an assertion.")

    def test_average_of_one_value(self):
        self.fail("Replace this line with an assertion.")

    def test_average_rejects_empty_list(self):
        self.fail("Replace this line with an assertion using assertRaises.")


if __name__ == "__main__":
    unittest.main()