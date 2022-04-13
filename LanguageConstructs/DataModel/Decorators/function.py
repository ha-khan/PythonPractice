# function decorators

import time
from functools import cache

def log(func):
    def decorator(*args):
        print("Processing computation")
        result = func(*args)
        print("Processing complete")
        return result
    return decorator

def measure(func):
    def decorator(*args):
        before = time.time()
        result = func(*args)
        after = time.time()
        print(f'Elapsed Time:{after - before} seconds')
        return result
    return decorator

class Orchestrator:
    def __init__(self) -> None:
        pass

    @cache
    @log
    @measure
    def computation(self, a, b) -> int:
        """
        order of decoration 
            cache(log(measure(computation))) 
        """
        print(f'Running computation on ({a}, {b})')
        time.sleep(2)
        return a + b

def main():
    m = Orchestrator()
    try:
        assert m.computation(1, 2) == m.computation(1, 3)
    except AssertionError:
        assert m.computation(1, 2) != m.computation(1, 3)

if __name__ == '__main__':
    main()
