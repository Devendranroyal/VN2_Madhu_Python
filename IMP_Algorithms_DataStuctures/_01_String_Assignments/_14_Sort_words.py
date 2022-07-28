'''
Sort unique words alphanumerically
set() : converts any iterables to distinct (unique), sorted sequence
sorted() : sorts any iterable object and returns (sorted) list
'''
multiple_str = input('Enter multiple strings separated by , :')
words = [word for word in multiple_str.split(',')]
#print(words)
ch = sorted(list(set(words)))
final_str = ','.join(ch)
print('After Sorting :', final_str)

# asha,nikhil,akhil,nishi,shoba,jyothi,asha