# Do a reverse inorder traversal and keep the track of current visited node.
# Once we found the element, last tracked element would be our answer.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder_successor(root: Node, target_node):
    global next
    if root is None:
        return
    inorder_successor(root.right, target_node)
    if root.data == target_node.data:
        if next:
            print("Inorder Successor is {}".format(next.data))
        else:
            print("Inorder successor is None")
    next = root
    inorder_successor(root.left, target_node)


if __name__ == '__main__':
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.left = Node(4)
    b_tree.left.right = Node(5)
    b_tree.right.right = Node(6)
    next = None
    inorder_successor(b_tree, b_tree.left.right)
