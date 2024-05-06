from StackClass import Stack

stack = Stack()

#push elements
stack.push(10)
stack.push(20)
stack.push(30)


# Display all elements in the stack 
stack.display()

# Peek the top element
print("Top element:", stack.peek())  # Output will be: 30

# Pop elements
# print("Popped element:", stack.pop())  # Output will be: 30
# stack.display()  # Output will be: 20 -> 10 -> None

# # Pop more elements
# print("Popped element:", stack.pop())  # Output will be: 20
# print("Popped element:", stack.pop())  # Output will be: 10

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output will be: True