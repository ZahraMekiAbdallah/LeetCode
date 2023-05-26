from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      ''' Level by Level BFS'''
      if root == None:
          return []
    
      res = [[root.val]]
      q = deque([root])
      flag = True

      while q:
        temp = []
        for i in range(len(q)):
          node = q.popleft()
          if node.left: 
            q.append(node.left)
            temp.append(node.left.val)
          if node.right: 
            q.append(node.right)
            temp.append(node.right.val)
        
        if len(temp) > 0:
          if flag:
            res.append(temp[::-1])
            flag = False
          else:
            res.append(temp)   
            flag = True
      return res
            
          
          
        