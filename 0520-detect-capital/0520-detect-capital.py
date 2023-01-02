class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # return word.lower() == word or word.upper() == word or word == ''.join([word[0].upper(), word[1:].lower()])
        
        if len(word) < 2: return True
        if ord(word[0]) < 97:
            word = word[1:]
            return ord(max(word)) < 97 or ord(min(word)) >= 97
        else:
            return ord(min(word)) >= 97