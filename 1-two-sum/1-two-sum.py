class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mymap = {}
        for i in range(len(nums)):
            
            subtraction = target - nums[i]
            if(subtraction in mymap):
                return [mymap[subtraction], i]
            mymap[nums[i]] = i