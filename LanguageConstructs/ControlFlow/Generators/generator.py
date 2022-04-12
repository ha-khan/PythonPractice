from iterator import *

class reader:
    def __init__(self) -> None:
        self.buffer = 'abcdefghijklmnopqrstuvwxyz'

    def __iter__(self):
        """
            using the yield keyword turns this function to a generator function
            and allows us to return back to the caller whenever this function has
            read enough of some buffer, the next time this iterator is called, 
            the state is picked back up from where the yield left off

            lets us avoid creating a "position" variable that keeps track of where
            in the buffer the data has temporarily been stopped.

            can interleve code where the reader does some reading, then give up control to caller

            the caller can do some processing, and once done and give back control to generator function

            sequentially 
        """
        for rune in self.buffer:
            yield rune
    
    def setup(self):
        yield 1
        yield 2
        yield 3
        yield 4


def main():
    v = FindVowel('file.txt')
    
    delattr(v, 'reader')
    setattr(v, 'reader', 'abcdefghijklmnop')
    v.compute()

    print("Resetting reader")

    delattr(v, 'reader')
    setattr(v, 'reader', reader())
    v.compute()

    r = reader()

    # generator expr
    print([val for val in r.setup()])

if __name__ == '__main__':
    main()