class Solution:
    def lengthOfLastWord(self, s: str)->int :
        list=[]
        for i in s.split():
            list.append(i)
        return len(list[-1])

a=Solution()
print(a.lengthOfLastWord("Hello World"))