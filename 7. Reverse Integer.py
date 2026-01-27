class Solution:
    def reverse(self, x: int) -> int:
        if x<(-2)**31 or x>2147483647:
            return 0
        string=str(abs(x))[::-1] if  x>0 else f"-{str(abs(x))[::-1]}"
        if  (-2)**31<=int(string)<=2**31-1:
            return int(string)
        else:
            return 0
a=Solution()
print(a.reverse(1534236469))  

'''
ý tưởng :
tại hàm reverse hãy kiểm tra xem x có nằm trong khoảng (-2)^31->2^31-1 hay không nếu không thì return 0
tại hàm tring nó sẽ lấy dại chuỗi ký tự của giá trị tuyệt đối x : nếu x lớn hơn 0 thì không thêm dấu trừ và ngược lại
tương tự kiểm tra giá trị nguyên của string có nằm trong khoảng (-2)^31->2^31-1 hay không nếu không thì return 0 có thì trả về giá trị nguyên của string
kiến thức sử dụng abs(x)-> trả về giá trị tuyệt đối của 1 số

'''