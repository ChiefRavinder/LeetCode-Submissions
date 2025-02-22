class Solution:
    def sumZero(self, n: int) -> List[int]:
        temp=[0]*n
        if n%2==0:
            for i in range(0,n,2):
                temp[i]=i+1
                temp[i+1]=-(i+1)
        else:
            for i in range(1,n,2):
                temp[i]=i+1
                temp[i+1]=-(i+1)
        return temp

        