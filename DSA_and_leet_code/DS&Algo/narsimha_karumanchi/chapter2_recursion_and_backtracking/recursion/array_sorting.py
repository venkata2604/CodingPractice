arr = [1,2,3,4,5,6,7]


#############################################################################################################
# Aprroach 1

# temp_arr = []

# for i in range(len(arr)-1):
#     # print(i)
#     if arr[i] <= arr[i+1]:
#         temp_arr.append(True)
#     else:
#         temp_arr.append(False)
# if all(temp_arr):
#     print("elements are sorted", all(temp_arr))
# else:
#     print("elements are not sorted")

###############################################################################################################
# Approach 2
is_Sorted = True

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_Sorted = False

if is_Sorted:
    print("Array is sorted")

if not is_Sorted:
    print("Array is Not Sorted")

############################################################################################################

