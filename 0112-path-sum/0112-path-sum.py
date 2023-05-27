class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
      if not root:
        return False
      
      lst = [[root, root.val]]
      
      while lst:
        node, total = lst.pop() # pop form end
        if node.left == None and node.right == None and total == target: # "root-to-leaf"
          return True
        
        if node.left:
          lst.append([node.left, node.left.val+total])
        if node.right:
          lst.append([node.right, node.right.val+total])
        
      return False