class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val: # in same direction, go deep
                root = root.right
            elif p.val < root.val and q.val < root.val: # in same direction, go deep
                root = root.left
            else: # in different direction, stop here, no other common parents
                return root

# O(log n), O(1) = Time, Space