class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count = defaultdict(int)
        
        for p, c in trust:
            count[c] += 1
            count[p] -= 1
        
        for i in range(1, n+1):
            if count[i] == n-1:
                return i
        return -1
    
    #TC: O(n) + O(n) ~= O(n) --> to form graph and looping over 1 to n
    #SC: O(n) => using count