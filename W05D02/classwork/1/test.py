import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

hasCycle = Solution.hasCycle

# Initialize colorama
init(autoreset=True)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_cycle_linked_list(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    if pos == -1:
        return head
    
    last_node = current
    cycle_node = head
    for i in range(pos):
        cycle_node = cycle_node.next
    last_node.next = cycle_node
    
    return head

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(hasCycle(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([create_cycle_linked_list([3,2,0,4],1)], True)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([create_cycle_linked_list([1,2],0)], True)

    @timeout(2)
    def test_case_3(self):
        self.run_test([create_cycle_linked_list([1],-1)], False)
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([create_cycle_linked_list([2, 1, 4, 3, 6, 5, 8, 7, 10, 9],5)], True)

    @timeout(2)
    def test_case_5(self):
        self.run_test([create_cycle_linked_list([2, 1, 4, 3, 6, 5, 8, 7, 10, 9],-1)], False)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()