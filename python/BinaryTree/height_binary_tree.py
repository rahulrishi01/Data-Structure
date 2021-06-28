class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Traverse:
    def __init__(self, root):
        self.head = root

    def inorder(self):
        if self.head:
            self._inorder(self.head)
        else:
            print("Tree is Empty")

    def _inorder(self, root: Node):
        if not root:
            return
        self._inorder(root.left)
        print(str(root.data) + ' -> ')
        self._inorder(root.right)


class HeightTree:
    def __init__(self, root: Node):
        self.head = root

    def height(self):
        if self.head:
            return self._height(self.head)
        else:
            return 0

    def _height(self, root: Node):
        if not root:
            return 0
        else:
            return 1 + max(self._height(root.left), self._height(root.right))


class SizeTree:
    def __init__(self, root: Node):
        self.head = root

    def size(self):
        if self.head:
            return self._size(self.head)
        else:
            return 0

    def _size(self, root: Node):
        if not root:
            return 0
        else:
            return 1 + self._size(root.left) + self._size(root.right)


if __name__ == '__main__':
    binary_tree = Node(5)
    binary_tree.left = Node(3)
    binary_tree.right = Node(7)
    binary_tree.left.left = Node(2)
    binary_tree.left.right = Node(4)
    binary_tree.left.left.left = Node(1)
    binary_tree.right.left = Node(6)
    binary_tree.right.right = Node(8)
    b_traverse = Traverse(binary_tree)
    b_traverse.inorder()
    bt_height = HeightTree(binary_tree)
    print("Height of the Binary tree is: {}".format(bt_height.height()))
    bt_size = SizeTree(binary_tree)
    print("Size of the Binary tree is: {}".format(bt_size.size()))
