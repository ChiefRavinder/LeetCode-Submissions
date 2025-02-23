class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& rseats) {
        rseats.push_back({0,10});
        rseats.push_back({n+1,1});
        sort(rseats.begin(),rseats.end());
        
        int size = rseats.size();
        int count = 0;
        int skipRows,skipCols;
        for(int i=1;i<size;++i){
            if(rseats[i][0]>rseats[i-1][0]){    //If the previous cross is not in same row as current cross
                skipRows = rseats[i][0] - rseats[i-1][0];//Count no of empty rows
                count += 2*(skipRows-1);    //Case-A: Add 2 count for each empty row

                if(rseats[i-1][1]==1)//case-F
                    count+=2;
                else if(rseats[i-1][1]<6)//Case-G
                    count+=1;

                if(rseats[i][1]==10)//Case-H
                    count+=2;
                else if(rseats[i][1]>5)//case-I
                    count+=1;
            } else {    //If the previous cross is in the same row as current cross
                if(rseats[i-1][1]==1 and rseats[i][1]==10)//Case-B
                    count+=2;
                else if(rseats[i-1][1]<4 and rseats[i][1]>7)//Case-C
                    count+=1;
                else if(rseats[i-1][1]==1 and rseats[i][1]>5)//Case-D
                    count+=1;
                else if(rseats[i-1][1]<6 and rseats[i][1]==10)//Case-E
                    count+=1;
            }
        }
        return count;
    }
};