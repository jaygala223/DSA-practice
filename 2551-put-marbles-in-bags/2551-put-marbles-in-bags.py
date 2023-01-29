class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # traversals twice and sorting twice... using only one sort and traversing from behind k-1 times
        #TC: O(n) + O(2 * nlogn) + O(n) ~= O(n log n)
        #SC: O(2*n) -> can be optimized by using just one of sum1 and sum2
        #refer: https://www.youtube.com/watch?v=_Fsz8MjKO4s
        
        sum1, sum2, ans = [], [], 0
        
        for i in range(len(weights)-1):
            sum1.append(weights[i] + weights[i+1])
            sum2.append(weights[i] + weights[i+1])
            
        #sum1 -> stores min pairs
        sum1 = sorted(sum1)
        
        #sum2 -> stores max pairs
        sum2 = sorted(sum2, reverse = True)
        
        #for making k partitions...you only need to make 'K-1' cuts
        for i in range(k-1):
            ans += sum2[i]
            ans -= sum1[i]
        
        return ans