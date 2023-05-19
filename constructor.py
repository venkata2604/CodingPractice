class Point:
    def _init_(self, x, y):  # initialising objects
        self.x = x
        self.y = y

    def move(self):  # self is automatically added
        print("move")

    def draw(self):
        print("draw")
        