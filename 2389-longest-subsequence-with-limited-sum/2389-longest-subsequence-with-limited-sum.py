class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        prefix = [0]
        
        for num in sorted(nums):
            prefix.append(prefix[-1] + num)
        
        return [bisect_right(prefix, q)-1 for q in queries]