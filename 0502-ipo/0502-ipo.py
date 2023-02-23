class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Time complexity: O(N log N + K log N) = O(N log N), where N is the number of projects and K is the number of projects that we can select. Sorting the "projects" vector takes O(N log N) time, and adding and removing elements from the priority queue takes O(log N) time. The while loop that adds the available projects to the priority queue runs at most N times, and the for loop that selects the projects to complete runs K times.
        # Space complexity: O(N + N) = O(N), where N is the number of projects. The space is used to store the "projects" vector. The priority queue used in the solution has a maximum size of N,

        
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        
        i = 0
        heap = []
        
        while k:
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                break
            
            w += -heapq.heappop(heap)
            k -= 1
        
        return w