from typing import List, Dict

class DAG:
    """
        Directed Acyclic Graph 
    """
    class Node:
        """
            Outer class repr the DAG as the larger structure, but which is itself a composite 
            of many nodes and as such the class shouldnt be exported outside, generally 
        """
        def __init__(self, value: int) -> None:
            self.value = value
            self.edges = []
        
        def insert(self, n):
            self.edges.append(n)
        
    def __init__(self, init: List[tuple[int, int]]) -> None:
        """
            TODO: need to add a validation check on whether input
                  contains a cycle, which goes against the DAG invariant
        """
        self.cache = {}
        for (src, dst) in init:
            if src not in self.cache and dst not in self.cache:
                s = DAG.Node(src)
                d = DAG.Node(dst)
                s.insert(d)
                self.cache[src] = s
                self.cache[dst] = d
            elif src not in self.cache:
                s = DAG.Node(src)
                d = self.cache[dst]
                s.insert(d)
                self.cache[src] = s
            elif dst not in self.cache:
                s = self.cache[src]
                d = DAG.Node(dst)
                s.insert(d)
                self.cache[dst] = d
            else:
                s = self.cache[src]
                d = self.cache[dst]
                s.insert(d)

    def __repr__(self) -> str:
        buffer = '' 
        for (key, val) in self.cache.items():
            buffer += f'{key} --> {sorted([x.value for x in val.edges])}\n'
        return buffer

    def topological_sort(self) -> str:
        buffer = ''
        return buffer
    
    def dfs(self) -> str:
        return ""
    
    def bfs(self) -> str:
        return ""
    
    # def __iter__(self):
    #     pass

def main():
    print("Constructing DAG")

    #
    #    1 ---> 3 ---> 4
    #     \     ^ 
    #      \   /
    #       v / 
    #        2
    #
    dag = DAG([(1, 3), (1, 2), (2, 3), (3, 4)])
    print(dag)

if __name__ == '__main__':
    main()