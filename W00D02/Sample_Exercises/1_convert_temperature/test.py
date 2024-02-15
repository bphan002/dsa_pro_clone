import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

convertTemperature = Solution.convertTemperature

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(convertTemperature(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([36.50], [309.65000,97.70000])
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([122.11], [395.26000,251.79800])
    
    @timeout(2)
    def test_case_3(self):
        self.run_test([91.55], [364.70000,196.79000])

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()