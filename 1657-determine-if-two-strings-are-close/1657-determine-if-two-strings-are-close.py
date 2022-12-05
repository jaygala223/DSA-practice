class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        freq1 = dict(collections.Counter(word1))
        freq2 = dict(collections.Counter(word2))
            
        c1 = sorted(freq1.values())
        c2 = sorted(freq2.values())

        return c1 == c2 and set(word1) == set(word2)