
# id()
# hash()
# __mro__
# __basis__
# __name__
# __class__

class Orchestrator:

    # class attribute; global to 
    instance_counter = 0

    def __init__(self, type: str) -> None:

        # need to use Orchestrator class instance attribute selector
        # to access class variables, in this scope 
        cls = self.__class__
        
        cls.instance_counter += 1

        # instance attribute
        self.type = type 
        
        pass

    def check_state(self):
        print("checking state ...")
        print("state check ok.")
        if not True:
            raise Exception

    @classmethod 
    def get_instance_count(cls) -> int:
        return cls.instance_counter

class VMOrchestrator(Orchestrator):
    """
        sub class from base orchestrator to orchestrate resources 
    """
    def __init__(self) -> None:
        """
            constructor 
        """
        print("init VMOrchestrator")

        # user super() to access direct parent class object
        # call its __init__, after this class's __init__ is finished executing
        # method resolution order (__mro__)
        super().__init__("VM")
    
    def check_state(self):
        print("checking VM state ...")
        # return super().check_state()

    def request_vm(self):
        try:
            self.check_state
        except:
            print("unable to request vm")

    def __del__(self):
        """
            destructor
        """
        print("releasing vm")

    @staticmethod
    def invoke(*args, **kwargs):
        for arg in args:
            print("invoke({})".format(arg))


def main():

    # Calls constructor; creates an instance object where we reference it with the label r
    r = VMOrchestrator()

    # pointer to object's class object
    # creates an instance object; not assigned to any label
    # since no reference will have destructor called
    r.__class__()

    # access class method by traversing up method resolution chain of VMOrchestrator class object
    print(VMOrchestrator.__mro__[1].__dict__['instance_counter'])
    VMOrchestrator.invoke(1, 2, 3, 4)
    r.invoke()

    # Calls direct base class's check_state method
    r.request_vm()

    assert VMOrchestrator.__name__ == 'VMOrchestrator'

    print(VMOrchestrator.get_instance_count())
    print(isinstance(r, VMOrchestrator))
    print(issubclass(VMOrchestrator, Orchestrator))

    # Calls destructor
    del r

if __name__ == '__main__':
    main()