class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        #dono strings mein at least ek 1 hona chahiye...otherwise nai convert kar sakte
        #dono all zero wali strings hui to same hi hogi...no need to convert
        return max(s) == max(target)