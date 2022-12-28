class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for item in piles:
            heapq.heappush(heap, -1*item)
        
        print(heap)
        
        while heap and k:
            top = -1 * heapq.heappop(heap)
            f = int(math.floor(top/2))
            heapq.heappush(heap, -1 * (top - f))
            k -= 1
        return -1 * int(sum(heap))