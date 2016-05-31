"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    
    '''
    #create the inserting node
    
    #traverse until the the pointer is pointing to the node previous of the inserting node
    
    #insert
    #set the next of the inserting node to be a temp_node
    #set the next of the previous to be the inserting_node
    #set the previous of the inserting_node to be the previous_node
    #set the previous of the temp_node to be the inserting_node
    #set the next of the inserting_node to be the temp_node
    
    '''
    
    insertingNode = Node(data)
    nodePointer = head
    atEnd = False
    
    if not nodePointer:
        #if None list
        insertingNode.prev = None
        insertingNode.next = None
        return insertingNode
    
    else:
        while(nodePointer.data < data):
            if nodePointer.next:
                nodePointer = nodePointer.next
            else:
                atEnd = True
                break
                
        if atEnd:
            #append at the end
            prevNode = nodePointer
            nextNode = None
            
            insertingNode.prev = prevNode
            insertingNode.next = nextNode
            
            prevNode.next = insertingNode
            
            
        else:
            nextNode = nodePointer
            prevNode = nodePointer.prev

            insertingNode.prev = prevNode
            insertingNode.next = nextNode

            if prevNode:
                prevNode.next = insertingNode
                
            nextNode.prev = insertingNode
            
    return head
  
