class Node:
    # Constructor 
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = None

    # Get and Set Methods
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    # get and set methods for next

    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    # Checking if the Linked List has next element
    def has_next(self):
        return self.next!= None


    



    