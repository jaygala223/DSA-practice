class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        idx = m + n - 1
        
        while(p1 >= 0 and p2 >= 0):
            if nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
            
            idx -= 1
        
        if p1 < 0:
            while p2 >= 0:
                nums1[idx] = nums2[p2]
                p2 -= 1
                idx -= 1
        else:
            while p1 >= 0:
                nums1[idx] = nums1[p1]
                p1 -= 1
                idx -= 1