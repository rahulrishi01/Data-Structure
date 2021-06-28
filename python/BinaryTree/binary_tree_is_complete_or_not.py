class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


def check_for_complete_tree(root: TreeNode) -> bool:
    if root is None:
        return True
    queue = []
    queue.append(root)
    flag = False
    while queue:
        node = queue.pop(0)
        if node.left:
            if flag:
                return False
            queue.append(node.left)
        else:
            flag = True
        if node.right:
            if flag:
                return False
            queue.append(node.right)
        else:
            flag = True
    return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    if check_for_complete_tree(root):
        print("Complete Binary Tree")
    else:
        print("NOT Complete Binary Tree")
