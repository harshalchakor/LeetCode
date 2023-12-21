# check is 't' tree is present in 's' as subtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def isSubTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        
        if self.sameTree(s, t):
            return True
        return (self.isSubTree(s.left, t) or 
                   self.isSubTree(s.right, t))
        
    
    def sameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
        return False
        
        
# First Tree         
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(4)
node1.right = TreeNode(5)
node1.right.left = TreeNode(6)
node1.right.left.left = TreeNode(7)
node1.right.left.right = TreeNode(8)
node1.right.right = TreeNode(9)

# subTree to check in first Tree
node2 = TreeNode(5)
node2.left = TreeNode(6)
node2.left.left = TreeNode(7)
node2.left.right = TreeNode(8)
node2.right = TreeNode(9)

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
printTree(node2)
print(arr1)
print(ans.isSubTree(node1, node2))
