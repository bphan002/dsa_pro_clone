import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

splitCircularLinkedList = Solution.splitCircularLinkedList

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
        output = splitCircularLinkedList(solution, *input_values)
        first = compare_cycle_lists(output[0], expected_value[0])
        second = compare_cycle_lists(output[1], expected_value[1])

        try:
            self.assertTrue(first and second)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([create_cycle_linked_list([1,5,7],0)], [create_cycle_linked_list([1,5],0),create_cycle_linked_list([7],0)])
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([create_cycle_linked_list([2,6,1,5],0)], [create_cycle_linked_list([2,6],0),create_cycle_linked_list([1,5],0)])

    @timeout(2)
    def test_case_3(self):
        self.run_test([create_cycle_linked_list([7,6,8,3,0,5],0)], [create_cycle_linked_list([7,6,8],0),create_cycle_linked_list([3,0,5],0)])
        
    @timeout(2)
    def test_case_4(self):
        self.run_test([create_cycle_linked_list([8,4,0,2,9,34,6],0)], [create_cycle_linked_list([8,4,0,2],0),create_cycle_linked_list([9,34,6],0)])

    def tearDown(self):
        result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()