class TreeNode:
    def __init__(self, key):
        self.key = key  # Value stored in the node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node


class BinaryTree:
    def __init__(self):
        self.root = None  # Reference to the root node of the tree

    def insert(self, key):
        if self.root is None:  # If the tree is empty, insert at the root
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)  # Call recursive insert method

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:  # If key is less than current node's key, go left
            if current_node.left is None:
                current_node.left = TreeNode(key)  # If left child is empty, insert here
            else:
                self._insert_recursive(current_node.left, key)  # Recursively insert on left subtree
        else:  # If key is greater than or equal to current node's key, go right
            if current_node.right is None:
                current_node.right = TreeNode(key)  # If right child is empty, insert here
            else:
                self._insert_recursive(current_node.right, key)  # Recursively insert on right subtree

    def search(self, key):
        return self._search_recursive(self.root, key)  # Call recursive search method

    def _search_recursive(self, current_node, key):
        if current_node is None:  # If node is None, key not found
            return False
        elif current_node.key == key:  # If key matches current node's key, found
            return True
        elif key < current_node.key:  # If key is less than current node's key, search left subtree
            return self._search_recursive(current_node.left, key)
        else:  # If key is greater than current node's key, search right subtree
            return self._search_recursive(current_node.right, key)


# Example usage:
tree = BinaryTree()  # Create a new binary tree

# Insert some values into the tree
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Search for a value in the tree
print(tree.search(6))  # Output: True
print(tree.search(9))  # Output: False
