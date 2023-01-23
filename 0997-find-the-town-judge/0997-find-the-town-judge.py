class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        
        for p, c in trust:
            indegree[c] += 1
            outdegree[p] += 1
        
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1