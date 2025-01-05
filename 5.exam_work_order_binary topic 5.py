class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert_recursive(node.right, key, value)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f'Key: {node.key}, Value: {node.value}\n')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(f'Key: {node.key}, Value: {node.value}\n')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f'Key: {node.key}, Value: {node.value}\n')

# Example usage
tree = BinaryTree()
tree.insert(1, 'Item 1')
tree.insert(2, 'Item 2')
tree.insert(3, 'Item 3')

print("Inorder traversal:")
tree.inorder(tree.root)

node = tree.search(2)
if node:
    print(f'Found: Key={node.key}, Value={node.value}')
else:
    print('Item not found')

tree.delete(2)
print("Inorder traversal after deleting key 2:")
tree.inorder(tree.root)

print("Minimum value in the tree:")
min_node = tree.find_min()
if min_node:
    print(f'Key: {min_node.key}, Value: {min_node.value}')
else:
    print('Tree is empty')

print("Maximum value in the tree:")
max_node = tree.find_max()
if max_node:
    print(f'Key: {max_node.key}, Value: {max_node.value}')
else:
    print('Tree is empty')

print("Preorder traversal:")
tree.preorder(tree.root)

print("Postorder traversal:")
tree.postorder(tree.root)
