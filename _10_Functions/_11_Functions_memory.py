
x = 10
print("x details : ", x, id(x))


# Function memory allocation

def get_data():   # Function invocation
    print("Welcome to my method")
    return "Hello World"
#1
print("Result is : ", get_data())
#2
result = get_data()   # Function calling
print("Result is : ", result)

# Print function name
print("Function details ", get_data, id(get_data))  # Get function body address
x = 10
print("X : ", x)
print("X : ", id(x))


# Mutable,Immutable :: Pass by value ,Pass by reference
# Copy : Shallow copy,Deep copy
# Lambda with map,filter,reduce functions
