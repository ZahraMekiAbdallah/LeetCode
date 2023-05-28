class Solution:
    
    # Recursive approach     
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
    
    # Iterative approach     
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
          return []
        
        res = []
        stack = [root]
        
        while stack:
          node = stack.pop()
          if node.left:
            stack.append(node.left)
          if node.right:
            stack.append(node.right)
          res.append(node.val)
        
        return res[::-1]













      
      
      
      
      
      
      
      
      
      
      