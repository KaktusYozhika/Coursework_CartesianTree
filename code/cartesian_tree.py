class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

def split(root, key):
    if not root:
        return (None, None)
    if key <= root.key:
        left, right = split(root.left, key)
        root.left = right
        return (left, root)
    else:
        left, right = split(root.right, key)
        root.right = left
        return (root, right)

def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right

def insert(root, key, priority):
    if not root:
        return Node(key, priority)
    if priority > root.priority:
        left, right = split(root, key)
        node = Node(key, priority)
        node.left = left
        node.right = right
        return node
    elif key < root.key:
        root.left = insert(root.left, key, priority)
    else:
        root.right = insert(root.right, key, priority)
    return root

def erase(root, key):
    if not root:
        return None
    if root.key == key:
        return merge(root.left, root.right)
    elif key < root.key:
        root.left = erase(root.left, key)
    else:
        root.right = erase(root.right, key)
    return root

def find(root, key):
    if not root:
        return False
    if key == root.key:
        return True
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)
