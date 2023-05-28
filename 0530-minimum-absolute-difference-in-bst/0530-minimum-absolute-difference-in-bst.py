class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # By using BFS only one way to visit the nodes line by line
        # But DFS 3 traversals can be applied, in BST to get min 
        # and we know that the lowest in left, so we can sort the array 
        # by inorder traversal

        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        lst = inorder(root)
        val = float('inf') 
        
        for i in range(len(lst)):
          for j in range(i+1, len(lst)):
            val = min(abs(lst[i] - lst[j]), val)
        
        return val

        

