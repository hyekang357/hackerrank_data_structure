"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
  
    '''
    for each node
    
        swap:
            change prev to next
            change next to prev
        
        go to the next node (node.prev)
    '''
    
    pointer = head
    while(pointer):
        temp_prev = pointer.prev
        pointer.prev = pointer.next
        pointer.next = temp_prev
        
        if not pointer.prev:
            break
            
        pointer = pointer.prev
        
        
    return pointer