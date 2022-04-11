# x = '''print(123)'''

# can turn this into a templated string and
# dynamically construct complex objects using arguments to 
# those string functions
x = "print(123)"
exec(x)

# Other languages have the concept of macros where at compile time 
# code would be generated and inserted at various portions onthe source



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
        self.__dict__['set_{}_utilization'.format(self.type)] = eval('lambda a: print(\'setting utilzation to: {}\'.format(a))') 
    
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

    def __init__(self, cpu, memory, network, storage) -> None:
        
        pass


def main():
    o = Orchestrator()

    Orchestrator.cpu.set_cpu_utilization(1)
    Orchestrator.memory.set_memory_utilization(1)
    Orchestrator.network.set_network_utilization(1)
    Orchestrator.storage.set_storage_utilization(1)



if __name__ == '__main__':
    main()
    
