nums = [1, 2, 3, 4]
numsref = nums
numsref[1] = 5
print(nums)
numscopy = nums.copy()
numscopy[3] = 6
print(nums)