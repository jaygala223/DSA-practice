class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        #TC: O(N*M) => going through n words with each of average length M
        #SC: O(26) => O(1) => since indexes will always have 26 elements which is constant
        
        indexes = {}
        
        for i, c in enumerate(order):
            indexes[c] = i
        
        for i in range(len(words)-1):
            j = 0
            w1, w2 = words[i], words[i+1]
            
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            
            for s1, s2 in zip(w1, w2):
                if indexes[s1] < indexes[s2]:
                    break
                if indexes[s1] > indexes[s2]:
                    return False

        return True