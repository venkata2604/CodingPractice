



def pathFinder(matrix, position, n):
    # returns a list of paths taken
    if position == (n-1, n-1):
        print("Reached final block")
        return [(n-1, n-1)]
    x,y = position
    if x+1 < n and matrix[x+1][y] ==1:
        a = pathFinder(matrix, (x+1, y), n)
        if a!=None:
            return [(x,y)]+a
    if y+1<n and matrix[x][y+1]==1:
        b = pathFinder(matrix, (x, (y+1)), n)
        if b!=None:
            return [(x,y)]+b
    return None


matrix = [[1,1,1,1,0],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,1,0,0,0],
          [1,1,1,1,1]]

print(pathFinder(matrix=matrix, position=(0,0), n=5))