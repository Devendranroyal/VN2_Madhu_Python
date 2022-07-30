'''

'''
li = []
for x in range(10):
    li.append(x)

print(li)


print([x for x in range(10)])  # print(10)

li = [x for x in range(10)]   # x = 10 print(x)
print(li)


li = []
for x in range(10):
    li.append(x ** x)
print(li)

print([x**x for x in range(10)])


li_eq = [x*x for x in range(10)]
print(li_eq)


'''
 http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

List comprehensions are a tool for transforming one list (any iterable actually) into another list.
 During this transformation, elements can be conditionally included in the new list and each element
  can be transformed as needed.
'''
