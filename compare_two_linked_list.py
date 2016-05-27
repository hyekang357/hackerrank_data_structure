#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    
    '''
    cases:
    headA and headB have same length and same data
    headA and headB have same length and different data
    headA and headB have different length
    '''
    
    nextA = headA
    nextB = headB
    while (nextA and nextB):
        if nextA.data != nextB.data:
            return int(False)
        nextA = nextA.next
        nextB = nextB.next
        
    return int(not nextA and not nextB)
  
  
  
  
  
  
  
  
