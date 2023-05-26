# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #Iterative BFS 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = 1
        q = deque([[root, l]])
        while q:
            node, level = q.popleft()
            if node.left or node.right:
              level+=1
            if node.left: 
              q.append([node.left, level])
            if node.right: 
              q.append([node.right, level])
            l = level
        return l

