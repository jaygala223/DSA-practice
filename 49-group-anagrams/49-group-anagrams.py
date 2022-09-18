class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        ans = []
        for word in strs:
            curr_word = word 
            sorted_word = ''.join(sorted(curr_word))
            #print(sorted_word)
            anagrams[sorted_word].append(curr_word)
        
        for key in anagrams:
            ans.append(anagrams[key])
        return ans
            