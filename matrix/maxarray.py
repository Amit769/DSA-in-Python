def maxSubarray(nums):
    max_sum = nums[0]
    current_sum = 0
    
    for i in range(len(nums)):
        
        current_sum = current_sum +nums[i]
        current_sum = max(current_sum, nums[i])
    
        if current_sum > max_sum:
             max_sum = current_sum
        
    
    
    return max_sum  
    
nums = list(map(int, input("enter the array: ").split()))
print("max sub array: ",  maxSubarray(nums))    