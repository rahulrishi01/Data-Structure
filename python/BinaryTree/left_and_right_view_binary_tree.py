# Left view of a binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def left_view(root: Node):
    t_queue = []
    t_queue.append(root)
    while len(t_queue) > 0:
        node = t_queue[0]
        print(node.data)
        t_queue.append(None)
        while t_queue[0] is not None:
            t_node = t_queue.pop(0)
            if t_node.left:
                t_queue.append(t_node.left)
            if t_node.right:
                t_queue.append(t_node.right)
        if t_queue[0] is None:
            t_queue.pop(0)


def right_view(root: Node):
    t_queue = []
    t_queue.append(root)
    while len(t_queue) > 0:
        node = t_queue[0]
        print(node.data)
        t_queue.append(None)
        while t_queue[0] is not None:
            t_node = t_queue.pop(0)
            if t_node.right:
                t_queue.append(t_node.right)
            if t_node.left:
                t_queue.append(t_node.left)
        if t_queue[0] is None:
            t_queue.pop(0)


if __name__ == '__main__':
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.right = Node(4)
    b_tree.right.left = Node(5)
    b_tree.right.right = Node(6)
    b_tree.right.left.left = Node(7)
    b_tree.right.left.right = Node(8)
    # left_view(b_tree)
    right_view(b_tree)
