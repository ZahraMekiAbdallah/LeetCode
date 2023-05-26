class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      q = deque([[root, 0]])
      res = 0
      while q:
        node, direction = q.popleft()
        if not node.left and not node.right and direction == 1:
          res+=node.val
        if node.left:
          q.append([node.left, 1])
        if node.right:
          q.append([node.right, 0])
      return res

            