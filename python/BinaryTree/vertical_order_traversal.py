class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Traverse:
    def __init__(self, root):
        self.head = root
        self.v_tree = {}

    def verical_order(self):
        if self.head:
            level = 0
            self._verical_order(self.head, level)
        else:
            print("Tree is Empty")
        for key in self.v_tree:
            print(self.v_tree[key])

    def _verical_order(self, root: Node, level):
        if not root:
            return
        if level in self.v_tree:
            self.v_tree[level] += [root.data]
        else:
            self.v_tree[level] = [root.data]
        self._verical_order(root.left, level + 1)
        self._verical_order(root.right, level - 1)


if __name__ == '__main__':
    binary_tree = Node(1)
    binary_tree.left = Node(2)
    binary_tree.right = Node(3)
    binary_tree.left.left = Node(4)
    binary_tree.left.right = Node(5)
    binary_tree.left.left.left = Node(8)
    binary_tree.left.left.right = Node(9)
    binary_tree.right.left = Node(6)
    binary_tree.right.right = Node(7)
    b_traverse = Traverse(binary_tree)
    # b_traverse.inorder()
    b_traverse.verical_order()
