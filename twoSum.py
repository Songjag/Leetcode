from calendar import c
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list={}
        for i,v in enumerate(nums):
            check=target-v
            if check in list:
                return [list[check],i]
            list[v]=i
        return []
a=Solution()
print(a.twoSum([3,2,3],6))                #fulltest
'''
Ý tưởng:
tại hàm def twonum khởi tạo 1 từ điển list
dùng hàm enumerate để phân tách các index:i và value :v
ví dụ với [3,2,3]
cho chạy vòng for thì : index=0,value=3 được chạy trong vòng lặp đầu tương tự với index=1 value=2 và index =2 value =3
```test.py
list=[1,2,3,4]
for i,v in enumerate(list):
    print(f"Index:{i}-Value:{v}")```
Output:
Index:0-Value:1
Index:1-Value:2
Index:2-Value:3
Index:3-Value:4
** Process exited - Return Code: 0 **



sau đó tạo 1 lính canh tên check=target(kết quả -giá trị của index),kiểm tra xem nó đã ở trong từ điển list hay chưa nêu chưa thì nó sẽ thêm vào list
với định dạng: list={1,0}
tiếp tục cho đến hết
nếu không có giá trị sẽ trả về []
'''
