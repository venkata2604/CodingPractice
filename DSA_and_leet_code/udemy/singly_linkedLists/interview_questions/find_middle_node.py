class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        # counter = 0
        p1 = self.head
        p2 = p1
        while p1 is not None and p1.next is not None:
            # p1 = p1.next
            # counter +=1
            # # print(p1.value, counter)
            # if counter % 2 != 0:
            #     p2 = p2.next 
            
            # Another way 
            p2 = p2.next
            p1 = p1.next.next
            
            
        return p2
            
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""