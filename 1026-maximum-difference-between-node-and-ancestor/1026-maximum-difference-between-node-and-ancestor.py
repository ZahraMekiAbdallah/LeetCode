# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        
        dic = defaultdict(list)
        
        while queue:
            node = queue.pop()
            if node.left:
                dic[node.left.val].append(node.val)
                dic[node.left.val] += dic[node.val]
                queue.append(node.left)
            if node.right:
                dic[node.right.val].append(node.val)
                dic[node.right.val] += dic[node.val]
                queue.append(node.right)
            
        max_num = 0
        for k,v in dic.items():
            if v:
                max_num = max(max_num, max(abs(k-item) for item in v))
        
        return max_num
                
        