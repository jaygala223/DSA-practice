class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unsigned int longContSubArr = 0;
        
        unsigned int sum = 0;
        unordered_map<int,int> mp;
        
        for(unsigned int i=0; i<nums.size(); i++){
            
            //1 hai to 1 add kar, varna -1 if its zero
            sum += (nums[i] == 0)? -1:1;
            
            auto it = mp.find(sum);
            
            if(sum == 0){
                longContSubArr = max(longContSubArr, i+1);
            }
            else if(it != mp.end()){
                longContSubArr= max(longContSubArr ,i-(mp[sum]));
            }
            else if(it == mp.end()){
                mp[sum] = i;
            }
        }
        return longContSubArr;
    }
};