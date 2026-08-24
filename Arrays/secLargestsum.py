def second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]
    
    
    for num in nums:
        
        
        if num > largest:
            second_largest = largest
            largest = num
    
        
        
        elif num > second_largest:
           second_largest = num    

    return second_largest      

nums = list(map(int, input("enter arr: ").split()))
print("second largest element: ", second_largest(nums))