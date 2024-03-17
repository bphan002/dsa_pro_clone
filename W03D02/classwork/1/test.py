import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

maxNumberOfApples = Solution.maxNumberOfApples

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(maxNumberOfApples(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[100,200,150,1000]], 4)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[900,950,800,1000,700,800]], 5)

    @timeout(2)
    def test_case_3(self):
        self.run_test([[1000, 900, 800, 500, 750]], 5)
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([[400, 250, 200, 150, 300, 400, 250, 200, 150, 300]], 10)
        

    def tearDown(self):
        result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()