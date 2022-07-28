'''
29. to set the indentation of the first line
Write a Python program to set the indentation of the first line.'''
import textwrap

mutliline_str = '''
Forever alone in a crowd, failed comedian Arthur Fleck seeks connection as 
he walks the streets of Gotham City. Arthur wears two masks -- the one 
he paints for his day job as a clown, and the guise he projects in a 
futile attempt to feel like he's part of the world around him.
'''
fline_indent = textwrap.fill(mutliline_str, initial_indent='      ', width=100)
# initial_indent if for first line
# subsequent_indent for other than 1st lines
print(fline_indent)
