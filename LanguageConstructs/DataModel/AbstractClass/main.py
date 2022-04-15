from abc import ABC, abstractmethod

# https://docs.python.org/3.9/library/collections.abc.html
# The cure for repetition is abstraction.


class Orchestrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def instantiate(self):
        """
            instantiate
        """
        pass

class VM(Orchestrator):
    def __init__(self, name: str):

        # https://docs.python.org/3/tutorial/classes.html#private-variables
        self.__name = name
        self.__alias_ = name

    def instantiate(self):
        print("instantiate")

def main():
    v = VM('resource')
    v.instantiate()
    try:
        print(v.__name)
    except:
        print(v._VM__name)
        print(v._VM__alias_)


if __name__ == '__main__':
    main()