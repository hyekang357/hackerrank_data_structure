#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
  
    prev = None
    curr = head
    
    while(curr):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    atNode = prev
    
    while(position != 0):
        position = position - 1
        atNode = atNode.next
        
    return atNode.data
        
  
  
  
  
  
  
  
  
  
