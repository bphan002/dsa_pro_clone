import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from solution import Solution

searchMatrix = Solution.searchMatrix

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(searchMatrix(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],3], True)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],13], False)

    @timeout(2)
    def test_case_3(self):
        self.run_test([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],7], True)

    @timeout(2)
    def test_case_4(self):
        self.run_test([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],16], True)

    @timeout(2)
    def test_case_5(self):
        self.run_test([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],35], False)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()