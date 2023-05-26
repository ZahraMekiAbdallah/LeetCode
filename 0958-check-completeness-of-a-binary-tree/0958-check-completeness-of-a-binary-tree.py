class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
      ''' As we should check level by level so will implement "BFS" 
      '''
      if not root:
        return True
      
      q = deque([root])
      nullFound = False
      
      while q:
        node = q.popleft()
        if node == None:
          nullFound = True
        else:
          if nullFound:
            return False
          else:
            q.append(node.left)
            q.append(node.right)
            
      return True
#       while q and q[0] is not None: # add children for all not none nodes
#         node = q.popleft()
#         q.append(node.left)
#         q.append(node.right)
        
#       while q and q[0] == None: # remove none nodes, so if remaining means missing before the most last left 
#         q.popleft()
              
#       return not q
        
      
            
        
