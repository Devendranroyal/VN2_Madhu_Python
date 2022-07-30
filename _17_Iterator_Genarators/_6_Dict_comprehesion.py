

vals = [1, 2, 3, 4, 5]
# REQ  OP : di = {1:1,2:4,3:9,4:16,5:25}

# For loop
di = {}
for each in vals:
    di[each] = each*each
print("Normal for loop   : ", di)

# Dict comprehension
di = {each: each*each for each in vals}

print("Dict comprehension: ", di)