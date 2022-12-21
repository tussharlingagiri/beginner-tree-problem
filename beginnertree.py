

class Tree:
    def __init__(self, value, left=None, right=None) -> None:
        self.value=value
        self.left=left
        self.right=right
        


root = Tree(3, Tree(4), Tree(5))

def check_sum(root):
    if root is None:
        return False
    if   root.left is None and root.right is None:
        return True
    return root.value == root.left.value + root.right.value
print (check_sum(root))


