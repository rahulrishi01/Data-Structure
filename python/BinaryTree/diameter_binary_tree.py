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


class Diameter:
    def __init__(self):
        self.height = 0

    def get_diameter(self, root: Node):
        if not root:
            return 0
        else:
            lh = HeightTree(root.left).height()
            rh = HeightTree(root.right).height()
            ldiameter = self.get_diameter(root.left)
            rdiameter = self.get_diameter(root.right)
            return max((lh + rh + 1), ldiameter, rdiameter)

    def get_diameter_opt(self, root: Node):
        if not root:
            return 0
        else:
            max_diameter = [-9999999]
            height = self._get_diameter_opt(root, max_diameter)
            return max_diameter[0]

    def _get_diameter_opt(self, root: Node, max_diameter):
        if not root:
            return 0
        else:
            lh = self._get_diameter_opt(root.left, max_diameter)
            rh = self._get_diameter_opt(root.right, max_diameter)
            max_diameter[0] = max(max_diameter[0], (1 + lh + rh))
            print(max_diameter[0])
            return 1 + max(lh, rh)

    def diameter_height(self, node: Node):
        if node is None:
            return 0, 0
        ld, lh = self.diameter_height(node.left)
        rd, rh = self.diameter_height(node.right)
        return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)

    def find_tree_diameter(self, node: Node):
        d, _ = self.diameter_height(node)
        return d


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
    bt_dia = Diameter()
    print("Diameter = {}".format(bt_dia.get_diameter_opt(binary_tree)))
    bt_diameter = Diameter()
    print("New Diameter = {}".format(bt_diameter.find_tree_diameter(binary_tree)))

