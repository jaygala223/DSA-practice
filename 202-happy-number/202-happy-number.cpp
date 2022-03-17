class Solution {
public:
    int squareAndSum(int num){
        int sum = 0;
        
        while(num){
            sum+= pow(num%10, 2);
            num = num/10;
        }
        return sum;
    }
    
    bool isHappy(int n) {
        int fast = n, slow = n;
        
        do{
            slow = squareAndSum(slow);
            fast = squareAndSum(fast);
            fast = squareAndSum(fast);
        }while(slow != fast);
        
        return fast == 1;
    }
};