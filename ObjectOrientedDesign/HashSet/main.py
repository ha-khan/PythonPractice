from abc import ABC, abstractmethod
import logging
from logging import DEBUG, INFO

class AbstractSet(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def get(self) -> bool:
        pass
    
    @abstractmethod
    def put(self):
        pass

class HashSet(AbstractSet):
    class List:
        """
            stores separate chaining in case of collision 
        """
        class Node:
            def __init__(self, value) -> None:
                self.next = None
                self.value = value

        def __init__(self, value) -> None:
            self.root = HashSet.List.Node(value)
            self.tail = self.root

        def append(self, value):
            self.tail.next = HashSet.List.Node(value)
            self.tail = self.tail.next
        
        def iterate(self):
            cursor = self.root
            while cursor is not None:
                yield cursor.value
                cursor = cursor.next
        
        def __repr__(self) -> str:
            buffer = ''
            cursor = self.root
            while cursor is not None:
                buffer += f'{cursor.value}->'
                cursor = cursor.next
                
            return buffer[:len(buffer)-2]
        
    def __init__(self, T: object, size: int, log_level=INFO) -> None:
        if T not in [int, str]:
            raise TypeError("Expected type to be either str or int!")
        
        if isinstance(T, int):
            self.T = int
        else:
            self.T = str

        self.table = [None for _ in range(size)]
        self.hash_func = eval(f'lambda x: x % {size}')

        logging.getLogger().setLevel(log_level)

    def get(self, value) -> bool:
        index = self.hash_func(value)
        entry = self.table[index]
        if entry is None:
            return False
        elif isinstance(entry, HashSet.List):
            for val in entry.iterate():
                if val == value:
                    return True
        return entry == value

    def put(self, value):
        index = self.hash_func(value)
        entry = self.table[index]
        if entry is None:
            self.table[index] = value 
        elif isinstance(entry, int):
            logging.debug('collision')
            # collision
            l = HashSet.List(entry)
            l.append(value)
            self.table[index] = l
        else:
            logging.debug('appending')
            # append to list
            entry.append(value)
        
        

def main():
    m = HashSet(int, 1000)
    m.put(2234)
    m.put(2360) 
    assert m.get(2234)
    assert m.get(2360)

if __name__ == '__main__':
    main()
