# Class for Node Definition
class Node:
    #constructor
    def __init__(self, data= None, next =None):
        self.data = data
        self.next = next

    # method for setting the data field of the node
    def setData(self, data):
        self.data= data

    # method for getting the data field of the node
    def getData(self):
        return self.data
    
    # method for setting next field of the node
    def setNext(self, next):
        self.next = next

    # method for getting next field of the node
    def getNext(self):
        return self.next
    

    # check if the current node is pointing to next node
    def hasNext(self):
        return self.next != None
    

    # Class for Linked List Definition
    class LinkedList(object):
        # initialising a list
        # constructor
        def __init__(self, node = None) -> None:
            self.length = 0
            self.head = node

        def length(self):
            current = self.head
            count = 0
            while current !=None:
                count = count+1
                current = current.next
                
    

    
