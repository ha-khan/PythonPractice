from abc import ABC, abstractmethod

# https://docs.python.org/3.9/library/collections.abc.html


class Orchestrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def instantiate(self):
        '''
            instantiate
        '''
        pass

class VN(Orchestrator):
    def __init__(self):
        pass

    def instantiate(self):
        print("instantiate")

def main():
    v = VN()
    v.instantiate()


if __name__ == '__main__':
    main()