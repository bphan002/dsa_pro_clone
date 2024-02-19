import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from example import Solution

add = Solution.add

#initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):
    def run_test(self, input_values, expected_values):
        solution = Solution()
        try:
            self.assertEqual(add(solution, *input_values), expected_values)
        except TimeoutError:
            self.fail()

    @timeout(2)        
    def test_case_1(self):
        self.run_test((2, 3), 1)

    @timeout(2) 
    def test_case_2(self):
        self.run_test((-1, 1), 2)

    @timeout(2) 
    def test_case_3(self):
        self.run_test((-1, 1), 5)
    
    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PSSED{Style.RESET_ALL}")

if __name__ == '__main__':
    unittest.main()        