class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        
        int n = nums1.size();
        
        unordered_set<int> set;
        
        for(int i=0; i<n; i++){
            set.insert(nums1[i]);
        }
        
        for(int i=0; i<nums2.size(); i++){
            if(set.find(nums2[i]) != set.end()) {
                ans.push_back(nums2[i]);
                set.erase(nums2[i]);
            }
        }
        return ans;
    }
};