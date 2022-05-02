class Solution {
public:
    int binarySearch(vector<int> arr, int target, bool leftBias){
        int left = 0, right = arr.size()-1;
        
        int pos = -1;
        
        while(left <= right){
            int mid = (left + right)/2;
            if (arr[mid] > target) right = mid - 1;
            else if(arr[mid] < target) left = mid + 1;
            else{
                pos = mid;
                if(leftBias) right = mid - 1;
                else left = mid + 1;
            }
        }
        return pos;
    }
    
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = binarySearch(nums, target, true);
        int r = binarySearch(nums, target, false);
        
        return {l,r};
    }
};