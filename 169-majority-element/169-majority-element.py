class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = cnt = 0
        
        for i in nums:
            if cnt == 0:
                ele = i
            if ele == i:
                cnt += 1
            else: cnt -=1
        
        return ele