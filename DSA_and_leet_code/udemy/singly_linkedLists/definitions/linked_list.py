class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenth = 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.lenth +=1

        return True
    
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            print("-->", end=' ')
            temp = temp.next


if __name__ == '__main__':
    my_ll = LinkedList(4)
    print("The first element of the linked list is: ")
    my_ll.print_ll()
    my_ll.append(8)
    my_ll.append(16)
    my_ll.append(32)
    print("all the elements of the linked list are ")
    my_ll.print_ll()


