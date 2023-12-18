# Fibonacci sequence like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def diameterOfTree(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2+left+right)
            return 1 + max(left, right)
        dfs(root)
        return res
            
root = TreeNode("5")
root.left = TreeNode("1")
root.left.left = TreeNode("6")
root.left.right = TreeNode("9")
root.right = TreeNode("3")
root.right.right = TreeNode("4")
root.right.left = TreeNode("2")
root.right.left.right = TreeNode("2")


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
