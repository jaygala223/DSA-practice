class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
        heap, result, time = [], [], 0
        for i, enqueueTime, processTime in sorted([(i, et, pt) for i, (et, pt) in enumerate(tasks)], key=lambda x: (x[1], x[2], x[0])):
            while heap and time < enqueueTime:
                nextTaskProcessTime, nextTaskIndex, nextTaskEnqueueTime = heapq.heappop(heap)
                result.append(nextTaskIndex)
                time = max(time, nextTaskEnqueueTime) + nextTaskProcessTime
            heapq.heappush(heap, (processTime, i, enqueueTime))
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result