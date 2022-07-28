
file = open("write_data1.txt", "w")
print("File path  :", file.name)
print("Mode       :", file.mode)
print("File closed?", file.closed)
file.close()
print("File closed?", file.closed)

print("-----I. Without  Context Manager-------------")
try:
    fobj = open("write_data1.txt", "w")
    fobj.write("Hello World.Python world")
except Exception as ex:
    print("Exception occured while handling file : ", ex)
finally:
    fobj.close()

print("Write operation completed")

print("-----II. With Context Manager-------------")

# fobj = open("write_data1.txt", "w")
# with RHS as LHS:
with open("write_data1.txt", 'w') as fobj:
    fobj.write("New data at last")

print("Write operation completed")

print("-----With Context Manager and Exception handling-------------")

try:
    # with RHS as LHS
    with open("C:/Users/madhu/Desktop/write_data2.txt", "w") as fobj:  # 11th line
        fobj.write("Hello World.Python world")
    print("Write operation completed")
except Exception as e:
    print("Exception occured during file hanlding : ", e)


class ContextManager:
    def __enter__(self):
        pass
    def __exit__(self):
        pass

