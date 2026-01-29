from typing import List 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=int("".join(str(x) for x in digits))+1
        list=[]
        for i in str(string):
            list.append(int(i))
        return list
        
a=Solution()
print(a.plusOne([1,2,3]))
        