''' Remove Duplicates '''

nums=[1,2,3,3,4,4,5]
new=[]
for i in nums:
    if i in new:
        continue
    else:
        new.append(i)
print(new)