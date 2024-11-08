def reverse(nums):
    new_array = []
    if len(nums) == 0:
        return []
    
    return [nums[-1]] + reverse(nums[:-1])

print(reverse([69, 87, 45, 21, 47]))