def kth_largest(nums, k):
      
    
        nums.sort()
        return nums[len(nums)-k ]
        
        
            
    

nums = list(map(int, input("enter the array: ").split()))
k = int(input("enter k: ", ))
print("kth largest number is :", kth_largest(nums))            