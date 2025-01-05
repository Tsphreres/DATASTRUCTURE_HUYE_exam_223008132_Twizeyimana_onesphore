class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def find_node(self, name):
        if self.name == name:
            return self
        for child in self.children:
            node = child.find_node(name)
            if node:
                return node
        return None

    def display(self, level=0):
        indent = ' ' * (level * 4)
        print(f"{indent}{self.name}: {self.data}")
        for child in self.children:
            child.display(level + 1)


root = TreeNode('Store')


electronics = TreeNode('Electronics')
groceries = TreeNode('Groceries')
root.add_child(electronics)
root.add_child(groceries)


phones = TreeNode('Phones')
laptops = TreeNode('Laptops')
electronics.add_child(phones)
electronics.add_child(laptops)

apple = TreeNode('Apple', {'price': 999.99, 'stock': 10})
samsung = TreeNode('Samsung', {'price': 799.99, 'stock': 15})
phones.add_child(apple)
phones.add_child(samsung)


root.display()

found_node = root.find_node('Apple')
if found_node:
    print(f"Found node: {found_node.name}, Data: {found_node.data}")
else:
    print("Node not found")
