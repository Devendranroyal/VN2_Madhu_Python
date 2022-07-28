'''
26.display formatted text (width=50) as output
Write a Python program to display formatted text (width=50) as output.
'''
import textwrap
python_intro ='''Python was created by Guido van Rossum during 1985- 1990. Python is a general-purpose interpreted, 
interactive, object-oriented, and high-level programming language. '''


print(textwrap.fill(python_intro, width=30))

#my_wrap = textwrap.TextWrapper(width = 20)
wrap_list = textwrap.TextWrapper(width = 20).wrap(text=python_intro)
for i in wrap_list:
    print(i)