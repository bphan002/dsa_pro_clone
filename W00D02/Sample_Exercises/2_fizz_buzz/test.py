import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution


fizzBuzz = Solution.fizzBuzz

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(fizzBuzz(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([3], ["1","2","Fizz"])
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([5], ["1","2","Fizz","4","Buzz"])
    
    @timeout(2)
    def test_case_3(self):
        self.run_test([15], ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()