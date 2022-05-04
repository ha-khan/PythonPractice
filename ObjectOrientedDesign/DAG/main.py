from typing import List, Callable

class DAG:
    """
        Directed Acyclic Graph 

        allows us to model/describe dependency relations between objects
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
        
    def __init__(self, init: List[tuple[int, int]], eval_func=print) -> None:
        """
            default contructor 
        """
        if not callable(eval_func):
            raise Exception('Given eval_function is not callable!') 
        self.eval_func = eval_func

        # val -> Node (reference)
        # assumption here is that each val would be unique to simplify things
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

    def topological_sort(self) -> None:
        """
          structured somewhat in a strategy pattern way
          
          DFS, BFS ultimately drives the topological_sort
        """
        seen = set()
        for _, node_reference in self.cache.items():
            if id(node_reference) not in seen:
                self.dfs(node_reference, seen)
    
    def dfs(self, root, seen):
        def _dfs(cursor):
            # if node already visited then stop this recursion
            if id(cursor) in seen:
                return
            
            # mark node as seen and continue traversal
            seen.add(id(cursor))
            for node in cursor.edges:
                _dfs(node)

            # evaluate
            self.eval_func(cursor.value)
        _dfs(root)
    
    def bfs(self, root, seen):
        from queue import Queue
        def _bfs(cursor):
            layer = Queue()
            layer.put(cursor)
            while not layer.empty():
                current_node = layer.get()
                for node in current_node.edges:
                    if id(node) not in seen:
                        seen.add(id(node))
                        layer.put(node)
                self.eval_func(current_node.value)
        _bfs(root)
   
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
    dag.topological_sort()

    from sys import stdout
    stdout.write(repr(dag))

if __name__ == '__main__':
    main()
