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
        """
        def __init__(self, file_name: str) -> None:
            self.fs_reader = file_name
            self.position = 0
            self.buffer = ['abcdefg']
        
        def __next__(self):
            """
                Returns the next available element, raising StopIteration when there are no more elements
            """
            try:
                self.reader.read()
            except as Exception:
                pass
        
        def __iter__(self) -> Iterator:
            """
                Returns self an instance that implements the Iterator interface, 
                allows the iterators to be used where an iterable is expected (for loop) 
            """
            return self

    def __init__(self, file_name) -> None:

        # cleaner way to access names defined at StreamProcessor scope
        cls = self.__class__

        self.buffer = ""
        self.read_len = 3
        self.reader =  cls.Reader(file_name)
    
    def compute(self, substr: str):
        """
            drives the computation 
        """
        for comp in self.reader:
            self.computation(comp)
            pass


    @abstractmethod
    def computation(self, substr: str) -> None:
        print("computatio") 


def main():
    print("main")

if __name__ == '__main__':
    main() 