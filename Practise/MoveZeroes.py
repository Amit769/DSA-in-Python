def moveZeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            
nums = list(map(int, input("enter the array: ").split()))
moveZeroes(nums)
print(nums)            