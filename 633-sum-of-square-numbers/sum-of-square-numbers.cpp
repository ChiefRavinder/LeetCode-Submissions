#import <math.h> 
class Solution {
public:
    bool judgeSquareSum(int c) {
        int left=0;
        long long int right= int(sqrt(c));
        while (left<=right){
            long long int sum=pow(left,2)+pow(right,2);
            if (sum==c){
                return true;
            }
            else if(sum>c){
                right--;
            }
            else{
                left++;
            }
        }
        return false;
    }
};