class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ###https://www.youtube.com/watch?v=7Xeorb721LQ&t=735s
        ###https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/3070481/Python3-prefix-sum-%2B-frequency-table-(Explained)
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