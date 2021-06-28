class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def find_node(self, data, node):
        if self.data == data:
            node.append(self)
        if self.children:
            for child in self.children:
                child.find_node(data, node)
        return node

    def insert_node(self, parent_node, data):
        new_node = []
        new_node = self.find_node(parent_node, new_node)
        if new_node:
            node = new_node[0]
            node.add_child(TreeNode(data))
            print("Node Inserted")
        else:
            print("Node Not found")

    def find_level(self, data):
        check_node = []
        check_node = self.find_node(data, check_node)
        if check_node:
            node = check_node[0]
            level = node.get_level()
            print("Node Found")
            return level
        else:
            print("Node Not found")
            return -1

    def delete_node(self, data):
        pass


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.insert_node("Cell Phone", "Motorola")
    print(root.find_level("Motorola"))

    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
