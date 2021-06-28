class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def check_identical_recursive(root1: Node, root2: Node):
    if not root1 and not root2:
        return True
    return (root1 and root2) and (root1.data == root2.data) and check_identical_recursive(root1.left, root2.left) and \
           check_identical_recursive(root1.right, root2.right)


if __name__ == '__main__':
    # construct first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)

    # construct second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
    if check_identical_recursive(x, y):
        print("Both trees are Identical")
    else:
        print("Both trees are not identical")