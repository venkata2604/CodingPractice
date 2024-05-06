# class for defining a linked list

class LinkedList(object):
    #  Constructor 
    def __init__(self, node = None) -> None:
        self.length = 0
        self.head = node

    def length(self):
        count = 0
        current = self.head

        while current !=None:
            count = count +1
            current.next

        return count

