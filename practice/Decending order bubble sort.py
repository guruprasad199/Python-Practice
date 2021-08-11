# code in python to decending order the list 

# def sort(nums):
#     for i in range(len(nums) - 1, 0, -1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp

# nums = [5,3,56,4,1]
# sort(nums)
# print(nums)
# nums.reverse()
# print(nums)

nums = [5,3,56,4,1]
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                tem = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tem
sort(nums)
print(nums)
    


        

