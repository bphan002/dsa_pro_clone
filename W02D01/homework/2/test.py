import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

lengthOfLongestSubstringTwoDistinct = Solution.lengthOfLongestSubstringTwoDistinct

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(lengthOfLongestSubstringTwoDistinct(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test(["eceba"], 3)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test(["ccaabbb"], 5)
        

    def tearDown(self):
        result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()