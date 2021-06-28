class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if (left_res and right_res) or (root.data in [p, q]):
            return root
        else:
            return left_res or right_res


if __name__ == '__main__':
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.left = Node(4)
    b_tree.left.right = Node(5)
    b_tree.right.right = Node(6)
    lca = Solution().lowestCommonAncestor(b_tree, 4, 6)
    print(lca.data)
