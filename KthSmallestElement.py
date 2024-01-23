# Kth Smallest Element
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def KthSmallestElement(self, root: TreeNode, k: int) -> int:
        
        arr = []
        
        # Solution 1: Inorder Traversal on BST will give ascending order. Recurrsive Solution
        def traverseTree(root):
            
            if not root:
                return
            else:
                traverseTree(root.left)
                arr.append(root.val)
                traverseTree(root.right)
            
        traverseTree(root)
        print(arr)
        return arr[k -1]
        
        # Solution 2: Inorder Traversal on BST wusing stack iterative soluction
        
        stack = []
        n = 0
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            n = n + 1
            
            if n == k:
                return root.val
                
            root = root.right
            
        
            
root = TreeNode("4")
root.left = TreeNode("2")
root.left.left = TreeNode("1")
root.left.right = TreeNode("3")
root.right = TreeNode("8")
root.right.left = TreeNode("6")
root.right.left.left = TreeNode("5")
root.right.left.right = TreeNode("7")
root.right.right = TreeNode("10")

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
print(ans.KthSmallestElement(root, 3))
