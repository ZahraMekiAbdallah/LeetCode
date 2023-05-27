class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative         
        res = []
        stack = []
        
        while root or stack:
          while root:
            stack.append(root)
            root = root.left
          root = stack.pop()
          res.append(root.val)
          root = root.right
        
        return res
      
    # Recurise         
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
