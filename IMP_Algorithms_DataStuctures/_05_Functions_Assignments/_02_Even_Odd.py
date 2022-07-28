'''
print even and odd numbers
'''
list_of_nums = [38, 92, 62, 93, 65, 82, 47, 90, 72, 31, 38]
tup_of_nums = (45, 73, 78, 63, 92, 52, 61, 95, 64, 91, 74)


def even_odd(l):
    evens = []
    odds = []
    for i in l:
        if i%2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f'evens - {evens}')
    print(f'odds - {odds}')


if __name__ == '__main__':
    print('list_of_nums - ')
    even_odd(list_of_nums)
    print('tup_of_nums - ')
    even_odd(tup_of_nums)