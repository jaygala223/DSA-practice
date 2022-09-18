class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
          
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: return res