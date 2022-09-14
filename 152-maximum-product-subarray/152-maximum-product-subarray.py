class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        
        for num in nums:
            if num == 0:
                currMin = currMax = 1
                continue
          
            temp = num*currMax
            currMax = max(num, temp, num*currMin)
            currMin = min(num, temp, num*currMin)
            
            res = max(res, currMax, currMin)
        return res