import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

copyRandomList = Solution.copyRandomList

# Initialize colorama
init(autoreset=True)

class RandListNode:
    def __init__(self, val=0, next=None, random=None, index=0):
        self.val = val
        self.next = next
        self.random = random
        self.index = index
        
def create_rand_linked_list(arr):
    if not arr:
        return None
    
    head = RandListNode(arr[0][0], None, None, 0)
    current = head
    i_to_node = {None: None, 0: head}
    
    for i in range(1, len(arr)):
        new_node = RandListNode(arr[i][0], None, None, i)
        i_to_node[i] = new_node
        current.next = new_node
        current = current.next
    
    current = head
        
    for i in range(len(arr)):
        rand = arr[i][1]
        current.random = i_to_node[rand]
        if current.random:
            current.random.index = i_to_node[rand].index
        current = current.next
    
    return head

def print_rand_linked_list(head):
    values = []
    current = head
    while current:
        rand_node = current.random
        rand_idx = None
        if rand_node:
            rand_idx = rand_node.index
        values.append([current.val, rand_idx])
        current = current.next
    return f"Linked List output values: {values}"

def compare_rand_lists(head1, head2):
    # maybe there's a better way to do this? 
    # but this works since we can access all nodes with .next

    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None:
        
        # This ensures no nodes have the same mem location
        if curr1 == curr2:
            return False
        if curr1.val != curr2.val:
            return False
        
        rand1 = curr1.random
        rand2 = curr2.random
        
        if (not rand1 and rand2) or (rand1 and not rand2):
            return False
        
        if rand1 and rand2:
            if rand1.val != rand2.val:
                return False
        
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 != None or curr2 != None:
        return False

    return True

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()
        output = copyRandomList(solution, *input_values)

        try:
            print(print_rand_linked_list(output))
            self.assertTrue(compare_rand_lists(output, expected_value))
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        print('Test Case 1:')
        rand_list = create_rand_linked_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
        self.run_test([rand_list], rand_list)
    
    @timeout(2)
    def test_case_2(self):
        print('Test Case 2:')
        rand_list = create_rand_linked_list([[1,1],[2,1]])
        self.run_test([rand_list], rand_list)

    @timeout(2)
    def test_case_3(self):
        print('Test Case 3:')
        rand_list = create_rand_linked_list([[3,None],[3,0],[3,None]])
        self.run_test([rand_list], rand_list)
        
    @timeout(2)
    def test_case_4(self):
        print('Test Case 4:')
        rand_list = create_rand_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        self.run_test([rand_list], rand_list)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()