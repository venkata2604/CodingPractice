class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1

        return True
    
    def print_ll(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end='')
            print("-->", end='')
            temp = temp.next

        print("None", end='')

if __name__ == "__main__":
    my_linked_list = LinkedList(6)
    my_linked_list.append(9)

    my_linked_list.print_ll()

