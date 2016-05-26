
class Node(object):

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def print_node(self):
		print "data = " + str(self.data)


def main():

	node_1 = Node(1)
	node_2 = Node(2)
	node_3 = Node(3)


	node_1.next = node_2
	node_2.next = node_3


	head = node_1

	print "original data"
	node_1.print_node()
	head.print_node()

	node_1.data = 0
	print"changed data"
	node_1.print_node()
	head.print_node()






main()
  
  
  
  
