class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        preWords = set()
        
        # asc order of word length, since longer words are formed by shorter words
        words.sort(key = len)
        
        # for each short word start building preWords
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)
        
        return res
    
    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False
        
        dp = [False] * (len(string) + 1)
        dp[0] = True
        
        for i in range(len(string)+1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]