class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        st = set(words)
        
        for word in words:
            for i in range(1, len(word)):
                st.discard(word[i:])
                
        ans = 0
        for i in st:
            ans += len(i)+1
        return ans
        