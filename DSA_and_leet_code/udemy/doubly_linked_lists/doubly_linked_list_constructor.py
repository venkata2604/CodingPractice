class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if self.tail is not None:
                self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    """
    this method, works but inefficient.
    It is always efficient to evaluate whether the index is closer to head or tail. 
    As a doubly linked list can move in both forward and backward directions, it is 
    efficient to start from head or tail based on which side is the index closer. 
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # else:  # there is no need to write else, as we are returning None above. When the above code satisfies. the
        # code will not reach this part and will come our function in the above line
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    """

    # efficient way to get an element based on index
    def get(self, index):
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        print(type(temp))
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # self.head = temp.next # this works but people don't use this
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp  # this returns a node, But if we use temp.value it will return a number

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp   

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index <0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        before = self.get(index-1)
        after = self.get(index+1)

        new_node.prev = before
        new_node.after = after

        before.next = new_node
        after.prev = new_node

        self.length +=1

        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length-1:
            return self.pop_first()
        
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None

        self.length -=1

        return temp

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
            print("<-->", end='')
        # print("None")


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(7)
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.append(3)
    print("pop result", my_doubly_linked_list.pop())
    # print("pop result", my_doubly_linked_list.pop())
    # print("pop result", my_doubly_linked_list.pop())
    # print("pop result", my_doubly_linked_list.pop())
    print(my_doubly_linked_list.pop_first())

    print(my_doubly_linked_list.prepend(2))

    print(my_doubly_linked_list.print_list())
