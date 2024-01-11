# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [[root, root.val, root.val]]
        max_diff = 0
        
        while queue:
            node, low, high = queue.pop()
            
            high  = max(high, node.val)
            low  = min(low, node.val)
            max_diff = max(max_diff, high-low)
            
            if node.left:
                queue.append([node.left, low, high])
            if node.right:
                queue.append([node.right, low, high])
            
        
        return max_diff
                
        