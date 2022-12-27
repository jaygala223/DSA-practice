class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        n, ans = len(rocks), 0
        diff = [-1] * len(rocks)
        
        for i in range(n):
            diff[i] = capacity[i] - rocks[i]
        
        diff = sorted(diff)
        print(diff)
        
        for i in range(n):
            if diff[i] == 0:
                ans += 1
            elif diff[i] <= additionalRocks:
                ans += 1
                additionalRocks = additionalRocks - diff[i]
            else:
                break
        return ans