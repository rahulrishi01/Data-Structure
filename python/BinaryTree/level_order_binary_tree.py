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

    def level_order(self):
        if self.head:
            self._level_order(self.head)
        else:
            print("Tree is Empty")

    def _level_order(self, root: Node):
        bt_queue = []
        bt_queue.append(root)
        while bt_queue:
            node = bt_queue.pop(0)
            print(node.data)
            if node.left:
                bt_queue.append(node.left)
            if node.right:
                bt_queue.append(node.right)


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
    # b_traverse.inorder()
    b_traverse.level_order()