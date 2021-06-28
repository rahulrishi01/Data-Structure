# Left view of a binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Leetcode My solution
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        level = 0
        result = []
        current_level = [root, None]
        next_level = []
        while current_level:
            node = current_level.pop(0)
            if node:
                next_level.append(node.val)
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
            else:
                result.append(next_level.pop())
                next_level = []
                if current_level:
                    current_level.append(None)

        return result


class Traverse:
    def __init__(self, root: Node):
        self.head = root
        self.level_dict = {}

    def top_view(self):
        if self.head:
            level = 0
            self.level_dict.clear()
            self._top_view(self.head, level)
            for key in sorted(self.level_dict, reverse=True):
                print(self.level_dict[key][0])
        else:
            print("Tree is Empty")

    def _top_view(self, root: Node, level):
        if root is None:
            return
        if level in self.level_dict:
            self.level_dict[level].append(root.data)
        else:
            self.level_dict[level] = [root.data]
        self._top_view(root.left, level + 1)
        self._top_view(root.right, level - 1)

    def bottom_view(self):
        if self.head:
            level = 0
            self.level_dict.clear()
            self._top_view(self.head, level)
            print(self.level_dict)
            for key in sorted(self.level_dict, reverse=True):
                print(self.level_dict[key][-1])
        else:
            print("Tree is Empty")

    def _bottom_view(self, root: Node, level):
        if root is None:
            return
        if level in self.level_dict:
            self.level_dict[level].append(root.data)
        else:
            self.level_dict[level] = [root.data]
        self._top_view(root.left, level + 1)
        self._top_view(root.right, level - 1)


if __name__ == '__main__':
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.right = Node(4)
    b_tree.right.left = Node(5)
    b_tree.right.right = Node(6)
    b_tree.right.left.left = Node(7)
    b_tree.right.left.right = Node(8)
    bt_traverse = Traverse(b_tree)
    bt_traverse.top_view()
    print("==================")
    bt_traverse.bottom_view()
