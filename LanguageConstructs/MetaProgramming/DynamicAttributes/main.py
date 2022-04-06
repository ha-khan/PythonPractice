from typing import Any

class Orchestrator:
    def __init__(self) -> None:
        pass

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in vars(self):
            raise ValueError('name: {} already set!'.format(__name))
        
        self.__dict__[__name] = __value

    def add_lcm_operation(self, name, operation) -> None:
        """
            dynamically adds an attribute to a specific instance 
            of the Orchestrator class 
        """
        if name in vars(self):
            raise ValueError('name: {} already set!'.format(name))
        
        self.__dict__[name] = operation
    
def main():
    o = Orchestrator()

    apply = lambda a: print('applying {}'.format(a))

    o.add_lcm_operation('apply', apply)

    o.apply('yo')

    print(o.__dict__)
    print(Orchestrator.__dict__)

    print(hasattr(o, 'apply'))

    try:
        o.add_lcm_operation('apply', None)
    except ValueError as e:
        print(e)

    delete = eval('lambda a: print(\'deleting {}\'.format(a))')
    setattr(o, 'delete', delete)
    o.delete('a')

    try:
        o.delete = None
    except ValueError as e:
        print(e) 


    
    



if __name__ == '__main__':
    main()
