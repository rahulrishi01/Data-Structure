# Given a binary search tree (BST), Find the Lowest Common Ancestor (LCA) of tho given nodes in BST.
from .bst_basic_operations import Node


def lowest_common_ancestor_recur(root: Node, p:Node, q:Node):
    parent_val = root.key
    p_val = p.key
    q_val = q.key

    if p_val > parent_val and q_val > parent_val:
        return lowest_common_ancestor_recur(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        return lowest_common_ancestor_recur(root.left, p, q)
    else:
        return root


def lowest_common_ancestor_iter(root: Node, p:Node, q:Node):
    p_val = p.key
    q_val = q.key

    node = root
    while node:
        parent_val = node.key
        if p_val > parent_val and q_val > parent_val:
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            node = node.left
        else:
            return root
    return node