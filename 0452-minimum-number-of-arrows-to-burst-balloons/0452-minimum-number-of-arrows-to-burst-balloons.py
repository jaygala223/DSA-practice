class Solution:
    def findMinArrowShots(self, segments: List[List[int]]) -> int:
        segments.sort(key=lambda p: p[1])
        ans, arrow = 0, 0
        for [start, end] in segments:
            if ans == 0 or start > arrow:
                ans, arrow = ans + 1, end
        return ans