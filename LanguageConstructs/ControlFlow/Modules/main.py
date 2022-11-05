from helpers.client import * 

# imports happen once and are cached to be reused
from helpers.client import *
from helpers.client import *

try:
    import AbstractClass
except ImportError as e:

    # since AbstractClass is outside the default search path
    # need to update the default search path list
    # 1. The home directory of the program
    # 2. PYTHONPATH directories (if set)
    # 3. Standard library directories
    # 4. The contents of any .pth files (if present)
    # 5. The site-packages home of third-party extensions
    import sys
    sys.path.append('/home/hk/Python/PythonPractice/LanguageConstructs/ControlFlow')
    from AbstractClass.main import VM

def main():
    h = HTTP_Client('https://www.google.com')
    h.do()

    v = VM('resource')
    v.instantiate()

    # since this module is being imported, its __name__ will not be __main__
    # "this" module .. Modules.main will be given the __name__ as __main__ since it is
    # the top-level module that the python interpreter is starting with
    from helpers.client import __name__ as n
    print(n)

    # dir can be used to print 
    import AbstractClass
    print(dir(AbstractClass))
    print(dir(AbstractClass.main))

    from sys import modules
    print(modules)

    # https://docs.python.org/3/library/functions.html#import__

if __name__ == '__main__':
    main()
