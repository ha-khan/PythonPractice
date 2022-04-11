class Orchestrator():
    """
        property decorator would need to be set for each attribute
        which could result in a lot of duplicate code, especially is access control 
        is similar, idea is to restructure code to follow the descriptor pattern 

        rather than use the global setting of __setattr__/__getattr__/__delattr__

        which would be called using the top-level
        - setattr()
        - getattr()
        - delattr()
        - del
        - . (attribute access operator) 
    
    """
    def __init__(self) -> None:
        self._memory = 0

    @property
    def memory(self):
        """
            getter 
        """
        print("get memory")
        return self._memory
    
    @memory.setter
    def memory(self, val: int):
        """
            setter 
        """
        if val < 0:
            raise ValueError("Memory cannot be negative!")
        self._memory = val

    @memory.deleter 
    def memory(self):
        del self._memory

def main():

    o = Orchestrator()

    try:
        o.memory = -1024
    except ValueError as e:
        print(e)
        o._memory = 1024
        print(o.memory)

if __name__ == '__main__':
    main()