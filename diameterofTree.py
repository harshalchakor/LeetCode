# Fibonacci sequence like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def diameterOfTree(self, root: TreeNode) -> int:
        diameter = 0
        def dfs(root):
            
            if not root:
                return
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            
            diameter = max(diameter, left + right)
        return diameter
            
root = TreeNode("5")
root.left = TreeNode("1")
root.left.left = TreeNode("6")
root.left.right = TreeNode("9")
root.right = TreeNode("3")
root.right.right = TreeNode("4")
root.right.left = TreeNode("2")


ans = Answer()
print(ans.diameterOfTree(root))


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
