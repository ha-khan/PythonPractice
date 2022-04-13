#
# In Python, try/except is commonly used for control flow, and not just for error handling.
#
#
# try
# except
# else
#
#
# The built-in exception classes can be subclassed to define new exceptions; 
# programmers are encouraged to derive new exceptions from the Exception class 
# or one of its subclasses, and not from BaseException.

class CustomException(Exception):
    """
        try / except
            Catch and recover from exceptions raised by Python, or by you.

        try / finally
            Perform cleanup actions, whether exceptions occur or not.

        raise
            Trigger an exception manually in your code.
        
        assert
            Conditionally trigger an exception in your code.
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def func():
    raise CustomException('incorrect usage')

def func2(*args):
    print(len(args))

def main():
    try:
        #func()
        func2()
    except CustomException as e:
        print(e)
    else:
        print('Finished executing')

if __name__ == '__main__':
    main()