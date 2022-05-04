from abc import ABC, abstractmethod


class HashMap(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def put(self):
        pass

class StrHashMap(HashMap):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        pass

    def put(self):
        pass

class IntHashMap(HashMap):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        pass

    def put(self):
        pass
    

class Map:
    def __init__(self, T=int) -> None:
        if isinstance(T, int):
            self.driver = IntHashMap()
        elif isinstance(T, str):
            self.driver = StrHashMap()
        else:
            raise TypeError("Expected driver to be either Str or Int!")
        
    def get(self):
        self.driver.get()
    
    def put(self):
        self.driver.put()

def main():
    m = Map()

if __name__ == '__main_':
    main()
