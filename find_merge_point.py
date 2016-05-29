"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    
    #get count of headA
    count_headA = 0
    point_headA = headA
    while(point_headA):
        count_headA += 1
        point_headA = point_headA.next
    
    #get count of headB
    count_headB = 0
    point_headB = headB
    while(point_headB):
        count_headB += 1
        point_headB = point_headB.next
        
    move_head_by = count_headA - count_headB
 
    if move_head_by > 0:
        #adjust headA
        while(move_head_by > 0):
            move_head_by -= 1
            headA = headA.next
        
    elif move_head_by < 0:
        #adjust headB
        while(move_head_by < 0):
            move_head_by += 1
            headB = headB.next
            
    while(headA != headB):
        headA = headA.next
        headB = headB.next
    return headA.data
        
        
        
    
  
  
  
  
  
  
  
  
  
  
