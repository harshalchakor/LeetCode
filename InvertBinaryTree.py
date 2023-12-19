# Fibonacci sequence like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def InvertBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.InvertBinaryTree(root.left)
        self.InvertBinaryTree(root.right)
        return root
        
            
root = TreeNode("1")
root.left = TreeNode("2")
root.left.left = TreeNode("3")
root.left.right = TreeNode("4")
root.right = TreeNode("5")
root.right.left = TreeNode("6")
root.right.left.left = TreeNode("7")
root.right.left.right = TreeNode("8")
root.right.right = TreeNode("9")

ans = Answer()

arr1 = []

def printTree(root):
    if not root:
        return
    else:
        arr1.append(root.val)
        
    printTree(root.left)
    printTree(root.right)
printTree(root)
print(arr1)
arr1 = []
printTree(ans.InvertBinaryTree(root))
print(arr1)
