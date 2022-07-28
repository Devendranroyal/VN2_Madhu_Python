'''
Remove specified index from list and print
'''

employee_list = ['Asha', 'Nikhil', 'Akhil', 'Nishitha', 'Keerthi','Sindhu']
index = 2

def remove_index(emp_list, ind):
    updated_list = []
    for n,i in enumerate(emp_list,0):
        if not ind == n:
            updated_list.append(i)
    return updated_list

print('Updatedlist after removing index element', remove_index(employee_list, index))