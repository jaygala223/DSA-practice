class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def no_overlaps(freq, curr_str):
            selfcheck = [0]*26
            for c in curr_str:
                if selfcheck[ord(c) - ord("a")]: return False
                selfcheck[ord(c) - ord("a")] = 1
            
            for c in curr_str:
                if freq[ord(c) - ord("a")]: return False
            
            return True
        
        def helper(ind, freq, arr, ans):
            if ind == len(arr):
                return ans
            
            curr_str = arr[ind]
            
            if no_overlaps(freq, curr_str) == False:
                return helper(ind+1, freq, arr, ans)
            
            else:
                #mark curr str chars in freq
                for c in curr_str:
                    freq[ord(c) - ord("a")] += 1
                ans += len(curr_str)
                pick = helper(ind+1, freq, arr, ans)
                
                #backtrack for non pick
                ans -= len(curr_str)
                for c in curr_str:
                    freq[ord(c) - ord("a")] -= 1
                
                non_pick = helper(ind+1, freq, arr, ans)
                
                return max(pick, non_pick)
            
        return helper(0, [0]*26, arr, 0)