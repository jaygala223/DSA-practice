class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int sum = 0;
        
        for(auto num: arr){
            sum += num;
        }
        if(sum%3 != 0) return false;
        
        int partSum = sum/3;
        int numPart = 0, tempSum = 0;
        
        for(auto num: arr){
            tempSum += num;
            if(tempSum == partSum){
                numPart++;
                tempSum = 0;
            }
            //if return true;
        }
        return (numPart > 2);
    }
};