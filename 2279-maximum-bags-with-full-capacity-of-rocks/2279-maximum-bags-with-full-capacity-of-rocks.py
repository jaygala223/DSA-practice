class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        n, ans = len(rocks), 0
        diff = []
        
        for i in range(n):
            diff.append(capacity[i] - rocks[i])
        
        for d in sorted(diff):
            if d <= additionalRocks:
                ans += 1
                additionalRocks -= d
            else:
                break
        return ans