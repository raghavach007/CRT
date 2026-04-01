# def check_sorted(nums):
#     isasc = False
#     for i in range(len(nums)):
#         if nums[i] > nums[i+1]:
#             return False
#     return True

'''
Count frequency of elements
input: [1,2,3,4,1,2,5,2,4]
output: {1:2,2:3,3:1,4:2,5:1}
'''
arr = [1,2,3,4,1,2,5,2,4]
res = {}

for ele in arr:
    if ele not in res:
        res[ele] = 1
    else:
        res[ele] += 1
print(res)