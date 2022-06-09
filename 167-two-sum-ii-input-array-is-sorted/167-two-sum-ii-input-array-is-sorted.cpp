class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int right = numbers.size() - 1;
        vector<int> ans(2);
       
        int left = 0;
        
        while(left <= right){
            if(numbers[left] + numbers[right] > target) right--;
            else if(numbers[left] + numbers[right] < target) left++;
            else{
                ans[0] = left + 1;
                ans[1] = right + 1;
                break;
            }
        }
        
        return ans;
    }
};