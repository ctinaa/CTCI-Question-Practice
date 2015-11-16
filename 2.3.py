'''
11.15.15

Delete Middle Node: Implement an algorithm to delete a node in 
the middle of a singly linked list given only access to that node. 


'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

#creating the linked list
class LinkedList():
	#create a head 
    def __init__(self, head=None):
        self.head = head

   	def add_node(self, data):
    	new_node = Node(data)
        # Make this the next node if no head 
        if self.head == None:
            self.head = new_node
        # If there is a tail, move to new node 
        if self.tail != None:
            self.tail.next = new_node
        # New node becomes the tail
        self.tail = new_node
 
	def remove_node(self, value):
       

    def print_list(self):
       	

