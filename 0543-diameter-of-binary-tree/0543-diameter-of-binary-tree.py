class Solution:
    def __init__(self):
      self.diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:       
      self.dfs(root)
      return self.diameter
    
    def dfs(self, node):
      if not node:
        return 0
      
      left = self.dfs(node.left)
      right = self.dfs(node.right)
      self.diameter = max(self.diameter, left+right)
      
      return max(left, right)+1