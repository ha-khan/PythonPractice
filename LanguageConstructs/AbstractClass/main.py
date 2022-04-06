from abc import ABC, abstractmethod

# https://docs.python.org/3.9/library/collections.abc.html
# The cure for repetition is abstraction.


class Orchestrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def instantiate(self):
        '''
            instantiate
        '''
        pass

class VM(Orchestrator):
    def __init__(self):
        pass

    def instantiate(self):
        print("instantiate")

def main():
    v = VM()
    v.instantiate()


if __name__ == '__main__':
    main()