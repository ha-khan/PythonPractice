# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# list
# array
# bytearray
# memoryview

# https://docs.python.org/3/library/array.html#module-array
from array import array


def main():
    a = array('h', range(10))

    for idx, rune in enumerate(a):
        print(f'{idx}, {rune}')

    print(a + a is a)

if __name__ == '__main__':
    main()