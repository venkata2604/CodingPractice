class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)

        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.value)
            temp = temp.next



if __name__ == "__main__":
    my_stack = Stack(4)
    my_stack.print_stack()




