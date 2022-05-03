# class decorators


def singleton(cls):
    instances = {}
    def decorator(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return decorator

@singleton
class ResourceCheck:
    def __init__(self, resource: str) -> None:
        """
            class's are objects that implement __call__ and thus act 
            as functions in a sense or objects  
        """
        self.resource = resource
        print('called')

def main():
    r = ResourceCheck('cpu')
    rr = ResourceCheck('storage')

    assert r.resource == rr.resource

    print(dir(ResourceCheck))

    assert ResourceCheck.__name__ == 'decorator'

if __name__ == '__main__':
    main()
