'''
count of all the elements in the list

* sets do not take duplicate elements

'''

list_of_nums = [45, 23, 48,34, 98, 34, 82, 82, 34, 67]
count = set()

def count_elemnts(lst1):
    for i in lst1:
        c1  = (i, lst1.count(i))
        count.add(c1)   # Adding list to count set
    return count


if __name__ == '__main__':
    print(count_elemnts(list_of_nums))