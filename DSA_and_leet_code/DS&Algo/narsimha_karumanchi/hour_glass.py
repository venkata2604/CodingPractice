# skip elements in the hour glass 
import numpy as np
arr = [[-9, -9, -9,  1, 1, 1], 
       [0, -9,  0,  4, 3, 2],
       [-9, -9, -9,  1, 2, 3],
       [0,  0,  8,  6, 6, 0],
       [0,  0,  0, -2, 0, 0],
       [0,  0,  1,  2, 4, 0]]

hourglasses = []
def extract_hourglass(arr):
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hourglass = []
            hourglass.extend(arr[i][j:j+3])
            hourglass.extend([arr[i+1][j+1]])
            hourglass.extend(arr[i+2][j:j+3])
            hourglasses.append(hourglass)
    return hourglasses

def hour_glass_sum(arr):
    sum_arr =[]
    for i in range(len(arr)):
        sum_arr.append(sum(arr[i]))
    return sum_arr

def hour_glass_max(arr):
    return np.amax(arr)

if __name__ == "__main__":
    print(hour_glass_max(hour_glass_sum(extract_hourglass(arr))))