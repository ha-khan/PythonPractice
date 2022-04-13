import pprint

class Orchestrator:

    # limits ability to dynamically set attributes on instances of 
    # this class, saves memory as __dict__ dictionary is no longer needed
    # especially if instances of this class are in 6+ orders of magnitude
    __slots__ = ['cpu', 'memory', 'storage', 'network']

    def __init__(self) -> None:
        self.cpu = 1.5
        self.memory = 1024
        self.storage = 512
        self.network = 1000
    
def main():
    o = Orchestrator()

    try:
        setattr(o, 'IO', 123)
    except AttributeError as e:
        print(e)
        assert hasattr(o, '__dict__') == False
        pprint.pprint(dir(o))

    try:
        class VMO(Orchestrator):
            # limited to class definition its defined in (superclass, subclass, ..etc)
            __slots__ = ['disk']
            def __init__(self) -> None:
                super().__init__()
        setattr(VMO(), 'IO', 123)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
