import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

groupAnagrams = Solution.groupAnagrams

#Initialize colorama
init(autoreset=True)

#inherits from unittest.TestCase class
class TestExample(unittest.TestCase):
    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            # self.assertEqual(groupAnagrams(solution, *input_values), expected_value)
            self.assertEqual(sorted(list(map(sorted, groupAnagrams(solution, *input_values)))), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        # self.run_test([["eat","tea","tan","ate","nat","bat"]], [["bat"],["nat","tan"],["ate","eat","tea"]] )
        self.run_test([["eat","tea","tan","ate","nat","bat"]], sorted(list(map(sorted, [["bat"],["nat","tan"],["ate","eat","tea"]]))))
   
    @timeout(2)
    def test_case_2(self):
        self.run_test([[""]], [[""]])

    @timeout(2)
    def test_case_3(self):
        self.run_test([["a"]], [["a"]])
        
    def tearDown(self):
        print(self)
        result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()