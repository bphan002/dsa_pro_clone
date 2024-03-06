import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

maximum69Number = Solution.maximum69Number

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(maximum69Number(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([9669], 9969)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([9996], 9999)

    @timeout(2)
    def test_case_3(self):
        self.run_test([9999], 9999)
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([6], 9)

    
    def test_case_5(self):
        self.run_test([999996], 999999)

    def test_case_6(self):
        self.run_test([6666666], 9666666)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()