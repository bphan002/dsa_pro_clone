import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

gameResult = Solution.gameResult

# Initialize colorama
init(autoreset=True)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(gameResult(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([create_linked_list([2,1])], "Even")
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([create_linked_list([2,5,4,7,20,5] )], "Odd")

    @timeout(2)
    def test_case_3(self):
        self.run_test([create_linked_list([4,5,2,1])], "Tie")
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([create_linked_list([2, 1, 4, 3, 6, 5, 8, 7, 10, 9])], "Even")
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()