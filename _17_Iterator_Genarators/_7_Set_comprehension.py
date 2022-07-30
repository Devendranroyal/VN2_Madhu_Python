
# REQ OUTPUT : {1,4,9,16,25,36}

# For loops
set1 = set({})
for each in range(1, 7):
    set1.add(each*each)

print("Using normal for loop   : ", set1)

set1 = set({each*each for each in range(1,7)})

print("Using set comprehension : ", set1)