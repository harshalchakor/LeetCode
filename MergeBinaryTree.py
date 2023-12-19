# Fibonacci sequence like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def InvertBinaryTree(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        
        if not node1 and not node2:
            return None
        v1 = node1.val if node1 else 0
        v2 = node2.val if node2 else 0
        root = TreeNode(v1 + v2)
        
        root.left = self.MergeBinaryTree(node1.left if node1.left else None, node2.left if node2.left else None)
        root.right = self.MergeBinaryTree(node1.right if node1.right else None, node2.right if node2.right else None)
        
        return root
            
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(4)
node1.right = TreeNode(5)
node1.right.left = TreeNode(6)
node1.right.left.left = TreeNode(7)
node1.right.left.right = TreeNode(8)
node1.right.right = TreeNode(9)

node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.left.left = TreeNode(3)
node2.left.right = TreeNode(4)
node2.right = TreeNode(5)
node2.right.left = TreeNode(6)
node2.right.left.left = TreeNode(7)
node2.right.left.right = TreeNode(8)
node2.right.right = TreeNode(9)



ans = Answer()

arr1 = []

def printTree(node1):
    if not node1:
        return
    else:
        arr1.append(node1.val)
        
    printTree(node1.left)
    printTree(node1.right)

# Input    
printTree(node1)
print(arr1)

# Output
arr1 = []
printTree(ans.MergeBinaryTree(node1, node2))
print(arr1)
