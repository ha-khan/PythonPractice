from typing import Any

class Orchestrator:

    # __class__ Reference to the object's class 
    #
    # __dict__  Mapping that stores the writable attributes of an object or class
    #
    # __slots__ Attribute that may be defined in a class to limit the attributes its instances can have.
    #
    #
    def __init__(self) -> None:
        pass

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
            setattr() operator or . operator will always invoke this special method and "hook" in a 
            check to see if setting an attribute dynamically (monkey patch)  
        """
        if __name in vars(self):
            raise ValueError('name: {} already set!'.format(__name))
        
        self.__dict__[__name] = __value

    # causes infinite recursion
    # def __getattribute__(self, __name: str) -> Any:
        # if __name in vars(self):
        #     return self.__dict__[__name]
        # return vars(self)[__name]


def main():
    o = Orchestrator()

    apply = lambda a: print('applying {}'.format(a))

    # invokes __setattr__
    setattr(o,'apply', apply)
    print('Has attribute \'apply\' is {}'.format(hasattr(o, 'apply')))

    # invokes __getattr__
    o_apply = getattr(o, 'apply')
    o_apply('deployment')

    print(o.__dict__ == vars(o))
    print(o.__class__ == type(o))
    #print(Orchestrator.__dict__)

    try:
        setattr(o,'apply', None)
    except ValueError as e:
        print(e)

    delete = eval('lambda a: print(\'deleting {}\'.format(a))')
    setattr(o, 'delete', delete)
    o.delete('a')

    try:
        o.delete = None
    except ValueError as e:
        print(e)

    try:
        delattr(o, 'delete')
        o.delete('deployment')
    except AttributeError as e:
        print(e)

    print(dir(o))
    print(locals())
    print(globals())
    print(callable(Orchestrator))
    print(callable(o))
    print(isinstance(o, Orchestrator))

if __name__ == '__main__':
    main()
