# iteration when scanning datasets/streams that cannot fit in available virtual memory
# goal is to fetch/process the items lazily (one at a time on demand) instead of loading in
# entire/large chunks of the dataset
#
#
# lazy evaluation vs eager evaluation

from abc import ABC, abstractmethod
from typing import Iterator


# all()
# iter()
# next()
# 

class StreamProcessor(ABC):
    class Reader():
        """
            Reader implements the Iterator interface __next__, and __iter__ 

            An iterator is an object/pointer that allows you to "traverse" some 
            collection of elements using a uniform interface (for x in iterator: ...)
        """
        def __init__(self, file_name: str) -> None:
            self.fs_reader = file_name

            # keeps state information on where in the "buffer" we are after each successful _read()
            self.position = 0

            # buffer that acts as location of bytes that we are reading
            self.buffer = 'abcdefghijklmnopqrstuvwxyz'
        
        def __next__(self):
            """
                Returns the next available element, raising StopIteration when there are no more elements
            """
            try:
                # self._read() can be somekind of sync read op (network, disk, ..etc)
                # everytime we successfully read some byte(s) as per reads 
                return self._read()
            except IndexError:
                raise StopIteration
        
        def __iter__(self) -> Iterator:
            """
                Returns self, an instance that implements the Iterator interface, 
                allows the iterators to be used where an iterable is expected (for loop)

                maybe should reset the self.postion to 0 for each call to __iter__ 
            """
            return self
        
        def _read(self) -> str:
            if self.position > len(self.buffer):
                raise IndexError
            
            val = self.buffer[self.position]
            self.position += 1
            return val
            

    def __init__(self, file_name) -> None:

        # cleaner way to access names defined at StreamProcessor scope
        cls = self.__class__
        self.reader =  cls.Reader(file_name)
    
    def compute(self):
        """
            drives the computation 
        """
        for comp in self.reader:
            self.computation(comp)

    @abstractmethod
    def computation(self, substr: str):
        pass

class FindVowel(StreamProcessor):
    def __init__(self, file_name) -> None:
        super().__init__(file_name)
    
    def computation(self, substr: str) -> None:
        if substr in ['a', 'e', 'i', 'o', 'u', 'y']: print(f'{substr} is a vowel')

def main():

    v = FindVowel('file.txt')

    v.compute()

if __name__ == '__main__':
    main() 