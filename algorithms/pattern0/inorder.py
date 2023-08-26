class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# construct the following binary tree
#
#           1
#         /   \
#        2     3
#       / \   /
#      4   5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)


def inorder_traversal_iterative(root):
    result = []
    stack = []
    current_node = root

    while(current_node!=None or stack!=[]):
        while(current_node != None):
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        result.append(current_node.value)
        current_node = current_node.right
    return result

print(inorder_traversal_iterative(root))
