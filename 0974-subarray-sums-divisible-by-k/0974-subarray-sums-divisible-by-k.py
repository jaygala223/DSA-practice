class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        ans = 0
        
        remainderFreq = defaultdict(int)
        remainderFreq[0] = 1
        prefixSum = 0
        
        for n in nums:
            prefixSum += n
            
            remainder = prefixSum%k
            
            ans += remainderFreq[remainder]
            
            remainderFreq[remainder] += 1
        
        return ans