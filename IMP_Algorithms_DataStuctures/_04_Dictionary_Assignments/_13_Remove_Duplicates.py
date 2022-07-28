'''
Remove duplicates from Dictionary
'''
list_of_ids = [{"asha": 1}, {"nikhil": 2}, {"aakash": 3}, {"nikhil": 2}, {"akhil": 2}, {"neha": 3}]
count_of_color_shades = [{'red': 7}, {'yellow':4}, {'blue':72}, {'orange':2}, {'indigo' : 9}]


def remove_dups(lst1):
    res_list = []
    for i in range(len(lst1)):
        if lst1[i] not in lst1[i + 1:]:
            res_list.append(lst1[i])
    return res_list


if __name__ == '__main__':
    print("After removing duplicates: ",remove_dups(list_of_ids))
    print("After removing duplicates: ",remove_dups(count_of_color_shades))