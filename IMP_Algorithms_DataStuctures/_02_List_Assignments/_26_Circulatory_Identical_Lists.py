'''
Check circularly identical in two lists
'''

list1 = ['asha', 'nisha', 'ishu', 'niki', 'akhil']
list2 = ['nisha', 'ishu', 'niki', 'akhil' , 'asha']

# if both are lists are same it returns nothing
def cir_list(lst1, lst2):
    if set(lst1) - set(lst2)== set():
        print('circular lists are identical')

if __name__ == '__main__':
    cir_list(list1, list2)