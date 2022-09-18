class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list) #mapping freqs of str -> anagrams
        
        for string in strs:
            freq = [0]*26
            for c in string:
                freq[ord(c)-ord('a')] += 1
            
            anagrams[tuple(freq)].append(string)
        
        
        return anagrams.values()
            