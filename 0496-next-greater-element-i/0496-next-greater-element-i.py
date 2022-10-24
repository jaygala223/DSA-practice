class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        maps = {}
        ans = []
        
        for i in range(len(nums2)):
            
            #next greater number mila
            while stack and stack[-1] < nums2[i]:
                maps[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        while stack:
            maps[stack.pop()] = -1
        
        for item in nums1:
            ans.append(maps[item])
            
        return ans
        