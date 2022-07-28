'''
Check if the list contains the sublist or not
'''

li1 = [45, 67, 34, 78, 83, 92, 53, 62]
s2 = [34, 78, 83]
s3 = [ 34, 76, 39]


def sublist_check(l1, l2):
    if len(l2) == 0:
        return True
    elif len(l2) == 1:
        if l2[0] in l1:
            return True
    else:
        if l2[0] in l1:
            length = len(l2)
            ind1 = l1.index(l2[0])
            for i in range(1, length):
                ind1 += 1
                if l2[i] == l1[ind1]:
                    pass
                else:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    print('s2 subset of li1 - %s'%(sublist_check(li1, s2)))
    print('s3 subset of li1 - %s'%(sublist_check(li1, s3)))