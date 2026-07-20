'''Find largest number'''

# method 1

nums=[1,5,3,7,9]
largest=nums[0]
for i in range(len(nums)+1):
    if i==len(nums)-1:
        break
    else:
        if nums[i]>nums[i+1]:
            largest=nums[i]
        else:
            largest=nums[i+1]
print(largest)

# method 2

largest=nums[0]
for i in range[1:]:
    if i>largest:
        largest=i
print(largest)