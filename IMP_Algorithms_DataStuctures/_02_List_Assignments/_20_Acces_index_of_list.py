'''
Access index of list
'''

list1 = [45, 23, 56, 85, 38, 92, 18]

def indexing1(lst):
    for i in range(len(lst)):
        print(i, lst[i])

def index_comprehension(lst):
    print('List Comprehension')
    print([list((i, lst[i])) for i in range(len(lst))])


indexing1(list1)
index_comprehension(list1)
