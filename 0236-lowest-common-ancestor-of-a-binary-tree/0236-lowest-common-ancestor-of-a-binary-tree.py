class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        anc_dic = {root: None}

        while p not in anc_dic or q not in anc_dic:
            node = stack.pop()
            if node.left:
                anc_dic[node.left] = node
                stack.append(node.left)
            if node.right:
                anc_dic[node.right] = node
                stack.append(node.right)
            
        parents = set()
        while p:
            parents.add(p)
            p = anc_dic[p]
        
        while q and q not in parents:
            q = anc_dic[q]

        return q

        # =========  Recursive DFS solution
#         if not root:
#             return None 

#         if root == p or root == q:
#             return root

#         l = self.lowestCommonAncestor(root.left, p, q)
#         r = self.lowestCommonAncestor(root.right, p, q)

#         if l and r:  # 5, 1
#             return root
#         else:
#             return l or r # 5, 4 l=5, r=None




# O(N) time & space complexity 





