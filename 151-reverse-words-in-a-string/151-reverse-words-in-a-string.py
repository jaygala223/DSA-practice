class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        split = split[::-1]
        ans = ""
        for i in split:
            ans += i + " "
        return ans[:-1]