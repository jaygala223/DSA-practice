class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        partners = defaultdict(int)
        ans = 0
        
        #store partners
        for i in range(0, n-1, 2):
            partners[i] = i+1
            partners[i+1] = i
        
        for i in range(0, n-2, 2):
            if partners[row[i]] != row[i+1]:
                ans += 1
                #swapping
                temp = row.index(partners[row[i]])
                row[i+1],row[temp] = row[temp],row[i+1]
                
        return ans