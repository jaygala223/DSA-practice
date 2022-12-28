class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-stones for stones in piles]
        heapq.heapify(heap)
        
        for i in range(k):
            top = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -(top - top//2))
        return -sum(heap)
        