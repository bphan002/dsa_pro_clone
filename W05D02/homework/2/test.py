import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

insert = Solution.insert

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

def compare_cycle_lists(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None:
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
        if curr1.next == head1 or curr2.next == head2:
            break

    if curr1.next.val != curr2.next.val:
        return False
    return True
    
class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()
        soln = create_cycle_linked_list(expected_value,0)

        try:
            self.assertTrue(compare_cycle_lists(insert(solution, *input_values), soln))
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([create_cycle_linked_list([3,4,1],0),2], [3,4,1,2])
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([create_cycle_linked_list([],-1),1], [1])

    @timeout(2)
    def test_case_3(self):
        self.run_test([create_cycle_linked_list([1],0),0], [1,0])
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([create_cycle_linked_list([1,3,5],0),4], [1,3,4,5])

    @timeout(2)
    def test_case_5(self):
        self.run_test([create_cycle_linked_list([3,3,3,3],0),4], [3,3,3,3,4])
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()