# Fibonacci sequence like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def inorderTraversal(self, root: TreeNode) -> int:
        
        recursive Solution
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        return res
        
        # iterative Solution
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res
            
            
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
print(ans.inorderTraversal(root))
