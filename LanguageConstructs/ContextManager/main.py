
class FindString:
    """
        FindString implements the Context Manager interface __enter__, __exit__

        https://docs.python.org/3/library/contextlib.html 
    """
    def __init__(self) -> None:
        pass

    def __enter__(self):
        """
            returns recently created instance
        """
        print("entering")
        # idea is to setup some resources that need to be released 
        # which will happen in invocation of __exit__ called after
        # with scope 
        return self
    
    def __exit__(self, *args):
        print("exiting")
        print(args)
    
    def computation(self):
        print("computation")
    
def main():
    with FindString() as fp:
        fp.computation()

if __name__ == '__main__':
    main()