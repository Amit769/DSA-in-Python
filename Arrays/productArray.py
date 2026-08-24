def productarray(nums):
    result = [1] * len(nums)

    # Left products
    left_product = 1

    for i in range(len(nums)):
        result[i] = left_product
        left_product *= nums[i]

    # Right products
    right_product = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


nums = list(map(int, input("Enter the array: ").split()))

print("Product array:", productarray(nums))
       
 
