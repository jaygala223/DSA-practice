import math
class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_avg = 1e9
        ans = -1

        prefix, suffix = [0]*(n+1), [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]

        for i in range(n):
            # Calculate average of left part of array, index 0 to i.
            left_part_average = prefix[i + 1]
            left_part_average //= (i + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = suffix[i + 1]
            # If right part have 0 elements, then we don't divide by 0.
            if n-i-1 != 0:
                right_part_average //= (n - i - 1)

            curr_diff = abs(right_part_average-left_part_average)
            
            if curr_diff < min_avg:
                ans = i
                min_avg = curr_diff

        return ans