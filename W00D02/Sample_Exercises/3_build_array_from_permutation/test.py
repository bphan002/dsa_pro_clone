import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution


buildArray = Solution.buildArray

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(buildArray(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[0,2,1,5,3,4]], [0,1,2,4,5,3])
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[5,0,1,2,3,4]], [4,5,0,1,2,3])
    
    @timeout(2)
    def test_case_3(self):
        self.run_test([[11,1,13,4,15,9,5,8,12,0,10,7,6,2,14,3]], [7,1,2,15,3,0,9,12,6,11,10,8,5,13,14,4])

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()