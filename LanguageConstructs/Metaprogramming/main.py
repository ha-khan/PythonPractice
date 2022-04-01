# x = '''print(123)'''

# can turn this into a templated string and
# dynamically construct complex objects using arguments to 
# those string functions
x = "print(123)"

exec(x)
