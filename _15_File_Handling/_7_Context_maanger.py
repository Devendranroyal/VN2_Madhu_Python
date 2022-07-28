# https://www.geeksforgeeks.org/context-manager-in-python/
# Python program creating a
# context manager

class ContextManager:

    def __init__(self):
        print('OBJECT --- init method called')

    def __enter__(self):
        print('ENTER  --- enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('EXIT  --- exit method called')

print("---Before with-----")

with ContextManager() as f_obj:
    print('with line 1')
    print('with line 2')
    print('with line 3')

print("---After with-----")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print("File Manager : __init__")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File Manager : __enter__")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        print("File Manager : __exit__")

    # loading a file


with FileManager('context.txt', 'w') as f_obj:
    print("I am in CM : Before")
    f_obj.write('---Data written using manual context manager----')
    print("I am in CM : After")
    print("Is file closed1 ? ", f_obj.closed)

print("Is file closed2 ? ", f_obj.closed)


'''
txt* files
csv* files
excel* files
zip* files 
pdf files
images
audio files
video files
'''