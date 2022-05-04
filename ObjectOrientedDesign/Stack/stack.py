from queue import Empty, LifoQueue
from collections import deque
from typing import Any
from abc import ABC, abstractmethod

class AbstractStack(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod 
    def push(self, val: Any) -> None:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

class Stack(AbstractStack):
    def __init__(self)-> None:
        self.driver = LifoQueue()

    def push(self, val: Any) -> None:
        self.driver.put(val)
    
    def pop(self) -> Any:
        return self.driver.get_nowait()

def main():
    s = Stack()
    for num in range(10):
        s.push(num)
    
    def generate_pop() -> Any:
        while True:
            try:
                yield s.pop()
            except Empty:
                break 
    
    print([x for x in generate_pop()])
    print(issubclass(Stack, AbstractStack))

if __name__ == '__main__':
    main()
