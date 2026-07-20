''' Count the occurences '''

items = ["apple","banana","apple","orange","mango","apple"]
target="apple"
count=0
for i in items:
    if i==target:
        count+=1
print(count)