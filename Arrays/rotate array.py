# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
n =len(nums)
k=3
k=k %n
print(k)

nums[:]=nums[-k:]+nums[:-k]
print(nums)