from typing import List  

class DAG():
    '''
        Directed Acyclic Graph 
    '''
    class Node:
        '''
            Outer class repr the DAG as the larger structure, but which is itself a composite 
            of many nodes and as such the class shouldnt be exported outside, generally 
        '''
        def __init__(self, value: int) -> None:
            self.value = value
            self.edges = List[DAG.Node]

    def __init__(self, init: List[tuple[int, int]]) -> None:
        self.init = init

    def dfs(self, source: int, target: int) -> int:
        return -1

def main():
    print("Constructing DAG")
    dag = DAG([tuple([1, 3])])

if __name__ == '__main__':
    main()