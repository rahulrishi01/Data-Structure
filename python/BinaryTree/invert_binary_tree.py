# Do a reverse inorder traversal and keep the track of current visited node.
# Once we found the element, last tracked element would be our answer.
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

    def invert_tree(self, root: Node):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert_tree(root.left)
        self.invert_tree(root.right)


if __name__ == '__main__':
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.left = Node(4)
    b_tree.left.right = Node(5)
    b_tree.right.right = Node(6)
    bt_traverse = Traverse(b_tree)
    bt_traverse.level_order()
    print("===================================")
    bt_traverse.invert_tree(b_tree)
    bt_traverse.level_order()
