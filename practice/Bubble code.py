def guru(nums):
    for i in range(len(nums)-1, 0 , -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [4,3,6,2,7,1]
guru(nums)
print(nums)
