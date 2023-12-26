# Print the squares of the sorted list

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Answer():
    
    def PathSumTree(self, root: TreeNode, targetSum: int) -> bool:
        
        def dfs(node, currSum):
            if not node:
                return False
                
            currSum += node.val
            
            if not node.left and not node.right:
                return currSum == targetSum
                
            return (dfs(node.left, currSum) or 
                     dfs(node.right, currSum))
        
        return dfs(root, 0)
        
        
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
printTree(node1)
print(arr1)
print(ans.PathSumTree(node1, 15))
