class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Pop from an empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Peek from an empty stack")
        return self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
