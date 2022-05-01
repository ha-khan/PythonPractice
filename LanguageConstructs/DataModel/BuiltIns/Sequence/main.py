# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# Mutable Sequence Objects
# list
# array
# bytearray
# range

# Immutable Sequence Objects
# tuple
# str
# bytes

# https://docs.python.org/3/library/array.html#module-array
from array import array
from ast import expr_context
import random

def main():
    """
        enumerate()
        filter()
        len()
        map()
        max()
        min()
        pow()
        range()
        reversed()
        slice()
        sorted()
        sum()
        zip()
    """
    # https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes
    from collections.abc import Sequence, MutableSequence
    
    # arrays 
    a = array('h', range(10))
    for idx, rune in enumerate(a):
        print(f'{idx}, {rune}')
    print(2 in a)
    print(-1 not in a)
    print(min(a))
    print(max(a))
    print(f'{array.__name__} Subclass of Sequence: {issubclass(array, Sequence)}, Subclass of MutableSequence: {issubclass(array, MutableSequence)}')

    # lists
    def gen_random():
        count = 10
        while count > 0:
            yield random.randint(0, 1000)
            count -= 1
    list()
    # literal syntax
    r = [num for num in gen_random()]
    print(sorted(r))
    print(r)
    print(isinstance(r, list))
    print(f'{list.__name__} Subclass of Sequence: {issubclass(list, Sequence)}, Subclass of MutableSequence: {issubclass(list, MutableSequence)}')

    # bytearray
    import sys
    b = bytearray(b'0101010101010100101')
    print(0 in b)
    print(b'0' in b)
    print(sys.getsizeof(b[0]))
    print(sys.getsizeof(b'1'))

    # tuple
    t = tuple([1, 2])
    t = (1, 2)
    print(t[0])
    print(2 in t)
    try:
        print(hash(t))
        t[1] = 1
    except Exception as e:
        print(e)

    # bytes
    b = b'123' # literal
    
    # strings
    s = "'123'"  # literal, can embed unescape '
    s = '"123"'  # literal, can embed unescaped "
    s = """
This is a multi-line
string object, rather than
a single line 
one
        """
    s = "this" " is" " concatenated" 
    


    # for obj in [list, array, bytearray]:
    #     result = '__hash__' in dir(obj)
    #     print(f'obj: {obj.__name__} implements __hash__: {result}')
            
if __name__ == '__main__':
    main()
