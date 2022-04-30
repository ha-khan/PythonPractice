from abc import ABC, abstractmethod
from typing import Any, List

class Tree(ABC):
    class Node:
        def __init__(self, val: Any, left, right) -> None:
            self.val = val
            
            if len(left) == 0:
                self.left = None
            else:
                val, l, r = self.split(left)
                print(val, l, r)
                self.left = Tree.Node(val, l, r)
            
            if len(right) == 0:
                self.right = None
            else:
                val, l, r = self.split(right)
                print(val, l, r)
                self.right = Tree.Node(val, l, r)

        @staticmethod 
        def split(l: List[Any]):
            midpoint = int(len(l)/2)
            left = l[1:midpoint+1]
            right = l[midpoint+1:]
            
            return l[0], left, right


    def __init__(self, instance) -> None:
        if not self.validate_if_tree(instance):
            raise Exception('Given instance does not satisfy the contraints to be a Tree!')

    def validate_if_tree(self, instance) -> bool:
        return True
        
class BinaryTree(Tree):
    def __init__(self, l: List[Any]) -> None:
        cls = self.__class__
        val, left, right = cls.Node.split(l)

        print(val, left, right)
        self.root = cls.Node(val, left, right)

        # run validation
        super().__init__(self)
    
    def inorder_traversal(self) -> None:
        def dfs(cursor):
            if cursor is None:
                return
            dfs(cursor.left)
            print(cursor.val)
            dfs(cursor.right)
        
        dfs(self.root)

def main():
    b = BinaryTree([1, 2, 3, 4, 5])
    b.inorder_traversal()

if __name__ == '__main__':
    main()
