'''
28.to add a prefix text to all of the lines in a string
'''
import textwrap
mulitiline_str = '''
Forever alone in a crowd, failed comedian Arthur Fleck seeks connection as 
he walks the streets of Gotham City. Arthur wears two masks -- the one 
he paints for his day job as a clown, and the guise he projects in a 
futile attempt to feel like he's part of the world around him.'''

filled = textwrap.fill(mulitiline_str, 50)
# print(filled)
print(textwrap.indent(filled, '>>>'))