from typing import List


#print(xau([2,4,3]))
class Solution:
    def xau(self,list:list):
        ds="".join(str(x)for x in reversed(list))
        return int(ds)
    def addTwoNumbers(self,nums1:List,nums2:List):
        total=str(self.xau(nums1)+self.xau(nums2))
        list=[int(x)for x in total]
        return list
a=Solution()
print(a.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
'''
Ý tưởng code 
tạo hàm xâu tạo 1 ds chứa các ký tự được đảo ngược từ list sau đó trả về số nguyên tạo bởi ds
sau đó thực hiện total với nums1 nums2 rồi tương tự list

'''