"""Problem 7: Given nxn matrix of blocks with a source upper left block
we want to find a path from the source to the destination (the lower right back). We can only move downwards and to the left.
Also, a path is given by 1 and a wall is given by 0."""

def pathFinder(matrix, position, n):
    # returns a list of paths taken
    print("input Position -----------------", position)
    if position == (n-1, n-1):
        print("Reached final block")
        print("returning value", [(n-1, n-1)])

        return [(n-1, n-1)]
    x,y = position
    if x+1 < n and matrix[x+1][y] ==1:
        print(f"Found wall '{matrix[x+1][y]}' at: ", x+1,y)
        a = pathFinder(matrix, (x+1, y), n)
        if a!=None:
            print("Position2 ------------", position)
            print("returning value", [(x+y)]+a)
            return [(x+y)]+a
    if y+1<n and matrix[x][y+1]==1:
        print(f"Found wall '{matrix[x][y+1]}' at: ", x, y+1)
        b = pathFinder(matrix, (x, (y+1)), n)
        if b!=None:
            print("Position4 ------------", x,y+1)
            print("returning value", [(x+y)]+b)
            return [(x,y)]+b


matrix = [[0,1,1,1,0],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,1,0,0,0],
          [1,1,1,1,1]]

print(pathFinder(matrix=matrix, position=(0,0), n=5))


