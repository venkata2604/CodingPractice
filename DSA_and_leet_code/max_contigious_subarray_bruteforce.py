class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_max = 0
        max_value = max(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = nums[i:j+1]
                temp_max = sum(temp)
                if temp_max > max_value:
                    max_value = temp_max
        
        return max_value


# This solution exceeded time limit and has a time complexity of o(n2) as we have two for loops.
# Space Complexity: 