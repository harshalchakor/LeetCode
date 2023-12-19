class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Answer:
    def LowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root
        
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        
            
node1 = TreeNode(6)
node1.left = TreeNode(2)
node1.left.left = TreeNode(0)
node1.left.right = TreeNode(4)
node1.right = TreeNode(8)
node1.right.left = TreeNode(7)
node1.right.right = TreeNode(9)

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
printTree(ans.LowestCommonAncestor(node1, node1.left.left, node1.left.right))
print(arr1)
