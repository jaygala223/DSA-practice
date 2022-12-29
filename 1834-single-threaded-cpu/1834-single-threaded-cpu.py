class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        ans = []
        i = 0
        heap = []
        time = tasks[0][0]
        
        while len(ans) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap: #available tasks hai
                t, idx = heapq.heappop(heap)
                time += t
                ans.append(idx)
            elif i < len(tasks):
                time = tasks[i][0]
            
        return ans