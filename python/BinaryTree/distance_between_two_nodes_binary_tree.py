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

    def LCA(self, n1, n2):
        if self.head:
            lca = self._LCA(self.head, n1, n2)
            d1 = []
            d2 = []
            if lca:
                self.get_distance(lca, n1, d1, 0)
                self.get_distance(lca, n2, d2, 0)
            dist_between = d1[0] + d2[0]
            return dist_between
        else:
            print("Tree is Empty.")
            return None

    def _LCA(self, root: Node, n1, n2):
        if root is None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self._LCA(root.left, n1, n2)
        right = self._LCA(root.right, n1, n2)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right

    def get_distance(self, root: Node, node, dist, level):
        if root is None:
            return
        if root.data == node:
            dist.append(level)
            return
        self.get_distance(root.left, node, dist, level + 1)
        self.get_distance(root.right, node, dist, level + 1)


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
    dist = b_traverse.LCA(1, 8)
    print(dist)

