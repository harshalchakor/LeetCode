# Kth Smallest Element
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def isValidBST(self, root: TreeNode, k: int) -> int:
        
        def valid(root, left_limit, right_limit):
            
            if not root:
                return True
            if not (root.val > left_limit and root.val < right_limit):
                return False
            
            return (valid(root.left, left_limit, root.val) and
            valid(root.right, root.val, right_limit))
        
        return valid(root, float("-inf"), float("inf"))
        
            
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(5)
root.right.left.right = TreeNode(7)
root.right.right = TreeNode(10)

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
print(ans.isValidBST(root, 3))
