import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

minEatingSpeed = Solution.minEatingSpeed

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(minEatingSpeed(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[3,6,7,11],8], 4)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[30,11,23,4,20],5], 30)

    @timeout(2)
    def test_case_3(self):
        self.run_test([[30,11,23,4,20],6], 23)
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([[312884470],312884469], 2)
        

    def tearDown(self):
        result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()