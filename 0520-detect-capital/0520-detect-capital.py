class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return word.lower() == word or word.upper() == word or word == ''.join([word[0].upper(), word[1:].lower()])