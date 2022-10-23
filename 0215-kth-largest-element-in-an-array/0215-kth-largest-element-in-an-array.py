class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        for num in nums:
            heapq.heappush(heap, -1*num)
        for i in range(k-1):
            heapq.heappop(heap)
        
        return -1*heap[0]
        