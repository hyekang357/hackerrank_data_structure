
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    
    found_cycle = False
    single_pointer = head
    double_pointer = head
    
    while(single_pointer and double_pointer and double_pointer.next):
        
        #increment
        single_pointer = single_pointer.next
        double_pointer = double_pointer.next.next
        
        if single_pointer == double_pointer:
            found_cycle = True
            break
            
    return found_cycle
