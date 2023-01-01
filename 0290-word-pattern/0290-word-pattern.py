class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mappings = {}
        s = s.split(' ')
        letters_used = set()
        
        if len(s) != len(pattern): return False
        
        for i in range(len(pattern)):
            if s[i] not in mappings and pattern[i] not in letters_used:
                letters_used.add(pattern[i])
                mappings[s[i]] = pattern[i]
                s[i] = pattern[i]
            elif s[i] in mappings:
                s[i] = mappings[s[i]]
            else:
                s[i] = '!'
        
        st = "".join(s)
        print(mappings)
        print(st, pattern)
        
        return "".join(s) == pattern
        