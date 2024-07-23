def isValidExpression(expression):
    stack = []
    mappings = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for symbol in expression:
        if symbol in mappings:  # If the character is an closing symbol
            # Pop the topmost element from the stack, if it is non empty otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'
            # If the mappings for the opening bracket in our hash and the top of the stack don't match, return False
            if mappings[symbol] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(symbol)

    # In the end, if the stack is empty, then we have a valid expression. The stack won't be empty for cases like ((()
    return not stack


print(isValidExpression("([)]"))  # Output: False
print(isValidExpression("{{([][])}()}"))  # Output: True