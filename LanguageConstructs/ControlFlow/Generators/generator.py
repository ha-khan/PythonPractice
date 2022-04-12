from iterator import *

class reader:
    def __init__(self) -> None:
        self.buffer = 'abcdefghijklmnopqrstuvwxyz'

    def __iter__(self):
        """
            using the yield keywork turns this function to a generator function
            and allows us to return back to the caller whenever this function has
            read enough of some buffer, the next time this iterator is called, 
            the state is picked back up from where the yield left off
        """
        for rune in self.buffer:
            yield rune

def main():
    v = FindVowel('file.txt')
    
    delattr(v, 'reader')
    setattr(v, 'reader', 'abcdefghijklmnop')
    v.compute()

    print("Resetting reader")

    delattr(v, 'reader')
    setattr(v, 'reader', reader())
    v.compute()


    

if __name__ == '__main__':
    main()