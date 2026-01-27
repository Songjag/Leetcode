class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<(-2)**31 or x>2147483647:
            return 0
        string=str(x)[::-1]
        return True if string==str(x) else False
'''
ý tưởng:
tại hàm isPalindrome hãy kiểm tra xem x có nằm trong khoảng (-2)^31->2^31-1 hay không nếu không thì return 0
string là gán chuỗi cho x và đảo ngược nó
kiểm tra xem string có giống chuỗi x ban đầu không nếu có thì trả về True không thì False


'''