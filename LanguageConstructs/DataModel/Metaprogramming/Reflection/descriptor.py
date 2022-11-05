
def log(func):
    def decorate(*args):
        print('calling {} descriptor'.format(args[0].type))
        func(*args)
    return decorate


class Client():
    """
        pattern 


        Client is a Descriptor class allows us to share access control logic across multiple independent instances.

        use for descriptors is managing access to instance data. 
        
        The descriptor is assigned to a public attribute in the class dictionary 
        while the actual data is stored as a private attribute in the instance dictionary. 
        
        The descriptor __get__() and __set__() methods are triggered when the public attribute is accessed.

        Descriptors get invoked by the dot operator during attribute lookup.


        A Descriptor class implements an interface consisting of the following methods:
          __get__
          __set__
          __delete__
    """
    def __init__(self, type: str) -> None:
        self.type = type

    @log
    def __set__(self, obj, val) -> None:
        """
            self referse to Client() descriptor 

            obj refers to actual instance (in Orchestrator) to be set

            val is the value that will be checked upon by the __set__ 


        """
        if val <=0: raise ValueError('Value must be > 0') 
        
        setattr(obj, 'resource', val)

    @log
    def __get__(self, instance, objtype=None):
        return getattr(instance, 'resource')

    # def __delete__(self, instance):
    
    
class Orchestrator:
    """
        Orchestrator is the managed class where the descriptor instances are declared as class attributes 
    """
    # Descriptor class object instances
    cpu = Client('cpu') 
    memory = Client('memory')
    storage = Client('storage')
    network = Client('network')

    def __init__(self, c, m, n, s, name) -> None:

        # https://docs.python.org/3/howto/descriptor.html#overview-of-descriptor-invocation
        # The expression obj.x looks up the attribute x in the chain of namespaces for obj. 
        # If the search finds a descriptor outside of the instance __dict__, its __get__() method is invoked
        self.cpu = c        # calls cpu.__set__()
        self.memory = m     # calls memory.__set__() when assigning
        self.network = n
        self.storage = s
        self.name = name

    def __repr__(self) -> str:
        # invokes __set__
        return 'cpu: {}, memory: {}, storage: {}, network: {}'.format(self.cpu, self.memory, self.network, self.storage)


def main():
    try:
        o = Orchestrator(1, 1, 0, 1, "xyz")
    except ValueError as e:
        print(e)
        o = Orchestrator(1, 1, 1, 1, "xyz")
    
    print(repr(o))



if __name__ == '__main__':
    main()
    