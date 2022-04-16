import functools
from operator import mul

# The Python Data Model documentation lists seven callable types:
#   1. User-defined functions
#       Created with def statements or lambda expressions.
#
#   2. Built-in functions
#       A function implemented in C (for CPython), like len or time.strftime .
#
#   3. Built-in methods
#       Methods implemented in C, like dict.get .
#
#   4. Methods
#       Functions defined in the body of a class.
#
#   5. Classes
#       When invoked, a class runs its __new__ method to create an instance, then __in
#       it__ to initialize it, and finally the instance is returned to the caller. Because there
#       is no new operator in Python, calling a class is like calling a function. (Usually calling
#       a class creates an instance of the same class, but other behaviors are possible by
#       overriding __new__ .
#
#   6. Class instances
#       If a class defines a __call__ method, then its instances may be invoked as functions.
#
#   7. Generator functions
#       Functions or methods that use the yield keyword. When called, generator functions return a generator object.

def main():
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for idx, rune in enumerate(l):
        print(f'idx: {idx}, rune: {rune}')

    ll = [y for y in map(lambda x: x*2, l)]
    print(ll)

    lll = [z for z in filter(lambda x: x in ['aa', 'cc', 'ee', 'gg'], ll)]
    print(lll)

    l.append('h')
    llll = [a for a in zip(l, ll)]
    print(llll)

    print(sum([x for x in range(10)]))

    print(functools.reduce(mul, [x+1 for x in range(5)]))

    from functools import partial, reduce

    # partials allows to gen new functions with certains params 'frozen' as an input
    print([x for x in reversed(list(map(partial(mul, 4), range(1, 5))))])
    
if __name__ == '__main__':
    main()
