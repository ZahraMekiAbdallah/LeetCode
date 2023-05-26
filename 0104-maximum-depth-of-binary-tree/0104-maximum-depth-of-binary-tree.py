# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(maxDepth(root.right)+1, maxDepth(root.left)+1)

    # Backtracking DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r, l):            
            if not r: return l
            return max(dfs(r.left, l+1), dfs(r.right, l+1))
        return dfs(root, 0) 

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r):            
            if not r: return 0
            return 1 + max(dfs(r.left), dfs(r.right))
        return dfs(root) 

    #Iterative BFS 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = 0
        q = deque([[root, 1]])
        while q:
            node, level = q.popleft()
            if node.left: q.append([node.left, level+1])
            if node.right: q.append([node.right, level+1])
            l = level
        return l



