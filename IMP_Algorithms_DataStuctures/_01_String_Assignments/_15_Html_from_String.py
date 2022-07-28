'''
Create html from string
Create the HTML string with tags around the word(s)
'''
str1 = 'The dark Night'
    #str(input('Enter String data:'))


def add_tags(string, tag):
    return "<%s>%s</%s>"% (tag, string, tag)

print('Input string :', str1)
print('With HTML tags :', add_tags(str1, 'b'))
