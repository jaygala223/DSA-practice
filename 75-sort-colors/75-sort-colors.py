class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        
        for i in range(len(nums)):
            if(nums[i] == 0): zero += 1
            elif nums[i] == 1: one += 1
            else: two += 1
        
        j = 0
        while(zero):
            nums[j] = 0
            zero -=1
            j+=1
        
        while(one):
            nums[j] = 1
            j+=1
            one-=1
        
        while(two):
            nums[j] = 2
            j+=1
            two-=1