'''
replace last value of tuples in a list
'''
# check
# tup = (23, 65, 93, 'abcd', 67)

# remove last and concat with (ele ,)
# without ',' the element will be considered as int

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]


def replace_last(lst, rep_ele):
    lst = [t[0:-1] + (rep_ele,) for t in lst]
    return lst


if __name__ == '__main__':
    print('After replacing with 999 :',replace_last(l,999))
    print('After replacing with True : ',replace_last(l, True))