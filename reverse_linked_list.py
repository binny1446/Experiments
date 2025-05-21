class ListNode: # Akash
    def __init__(self, val=0, next=None): # Akash
        self.val = val # Akash
        self.next = next # Akash

def reverse_list(head): # Akash
    """ # Akash
    Given the head of a singly linked list, reverse the list, and return the reversed list. # Akash
    """ # Akash
    prev = None # Akash
    current = head # Akash
    while current: # Akash
        next_node = current.next # Akash
        current.next = prev # Akash
        prev = current # Akash
        current = next_node # Akash
    return prev # Akash

# Helper function to print linked list # Akash
def print_list(head): # Akash
    nodes = [] # Akash
    current = head # Akash
    while current: # Akash
        nodes.append(str(current.val)) # Akash
        current = current.next # Akash
    print(" -> ".join(nodes)) # Akash

# Test cases # Akash
if __name__ == "__main__": # Akash
    # Test 1: 1 -> 2 -> 3 -> 4 -> 5 # Akash
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))) # Akash
    print("Original list 1:") # Akash
    print_list(head1) # Akash
    reversed_head1 = reverse_list(head1) # Akash
    print("Reversed list 1:") # Akash
    print_list(reversed_head1) # Akash
    # Expected: 5 -> 4 -> 3 -> 2 -> 1 # Akash

    # Test 2: 1 -> 2 # Akash
    head2 = ListNode(1, ListNode(2)) # Akash
    print("Original list 2:") # Akash
    print_list(head2) # Akash
    reversed_head2 = reverse_list(head2) # Akash
    print("Reversed list 2:") # Akash
    print_list(reversed_head2) # Akash
    # Expected: 2 -> 1 # Akash

    # Test 3: Empty list # Akash
    head3 = None # Akash
    print("Original list 3:") # Akash
    print_list(head3) # Akash
    reversed_head3 = reverse_list(head3) # Akash
    print("Reversed list 3:") # Akash
    print_list(reversed_head3) # Akash
    # Expected: (empty) # Akash

    # Test 4: Single node list # Akash
    head4 = ListNode(1) # Akash
    print("Original list 4:") # Akash
    print_list(head4) # Akash
    reversed_head4 = reverse_list(head4) # Akash
    print("Reversed list 4:") # Akash
    print_list(reversed_head4) # Akash
    # Expected: 1 # Akash
