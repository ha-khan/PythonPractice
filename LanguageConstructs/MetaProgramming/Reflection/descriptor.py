

class Client():
    """
        pattern 


        Client is a Descriptor class allows us to share access control logic across multiple independent instances.


        A Descriptor class implements an interface consisting of the following methods:
          __get__
          __set__
          __delete__


    """
    def __init__(self, type: str) -> None:
        self.resource = 0
        self.type = type
    
    def __set__(self, instance, val) -> None:
        if val > 0:
            instance.__dict__[self.resource] = val
        else:
            raise ValueError("Value must be > 0")
    
    
    
class Orchestrator:
    """
        Orchestrator is the managed class where the descriptor instances are declared as class attributes 
    """
    # Descriptor instances
    cpu = Client("cpu") 
    memory = Client("memory")
    storage = Client("storage")
    network = Client("network")

    def __init__(self, cpu, memory, network, storage, name) -> None:
        self.cpu = cpu
        self.memory = memory
        self.network = network
        self.storage = storage
        self.name = name


def main():
    try:
        o = Orchestrator(1, 1, 0, 1, "xyz")
    except ValueError as e:
        print(e)
        o = Orchestrator(1, 1, 1, 1, "xyz")


if __name__ == '__main__':
    main()
    
