import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

minSetSize = Solution.minSetSize

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(minSetSize(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[3,3,3,3,5,5,5,2,2,7]], 2)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[7,7,7,7,7,7]], 1)

    @timeout(2)
    def test_case_3(self):
        self.run_test([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 5)
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([ [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]], 2)

    
    def test_case_5(self):
        self.run_test([[5]], 1)

    def test_case_6(self):
        self.run_test([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]], 3)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()