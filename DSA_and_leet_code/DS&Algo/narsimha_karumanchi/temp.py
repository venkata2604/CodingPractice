def hourglassSum(arr):
    # Write your code here
    hourglasses = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hourglass = []
            hourglass.extend(arr[i][j:j+3])
            hourglass.extend([arr[i+1][j+1]])
            hourglass.extend(arr[i+2][j:j+3])
            hourglasses.append(hourglass)
    sum_hourglass = []
    for k in range(len(hourglasses)):
        sum_hourglass.append(sum(hourglasses[i]))
    
    return sum_hourglass
        
