class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        occurence = {}
        
        for num in nums:
            if num in occurence:
                return True
            occurence[num] = True
        return False