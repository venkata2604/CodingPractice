class TwoSum:
    nums = []
    target = 0

    @staticmethod
    def bruteforce(nums, target):
        arr_length = len(nums)

        for i in range(arr_length - 1):
            for j in range(i + 1, arr_length):
                if target == nums[i] + nums[j]:
                    return [i, j]
        return []  # None

    @staticmethod
    def hashtable_two_pass(nums, target):
        numMap = {}

        # preparing a Hashmap of list
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for j in range(len(nums)):
            k = target - nums[j]

            if k in nums and k != nums[j]:
                return [j, numMap[k]]

        return []  # No Result

    @staticmethod
    def hashtable_one_pass(nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


obj = TwoSum()
# print(obj.bruteforce([1, 2, 3, 4], 5))
# print(obj.hashtable_two_pass([1, 2, 3, 4], 3))
print(obj.hashtable_one_pass([1, 2, 3, 4], 5))


