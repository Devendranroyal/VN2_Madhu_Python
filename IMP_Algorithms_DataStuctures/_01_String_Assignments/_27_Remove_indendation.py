'''
27. remove existing indentation from all of the lines in a given text
'''
import textwrap
multiline_str = '''
        After Gordon, Dent and Batman begin an assault
        on Gotham's organised crime, the mobs hire the Joker, 
        a psychopathic criminal mastermind who wants 
        to bring all the heroes down to his level.'''
final_str = textwrap.dedent(multiline_str)
# textwrap.indent() to give indentation  (min 2 parms)
# textwrap.dedent() to remove indentation
print(final_str)