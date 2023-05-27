class Solution:
    #Traverse Inorder (Left, Root, Right)
    
    #Iterative     
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        while root or stack:
          while root:
            stack.append(root)
            root = root.left
            
          root = stack.pop()
          k -= 1
          if k == 0:
            return root.val
          root = root.right
        
        return []
          
    # Recursive         
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrderTraverse(root):
            if not root:
              return []
            
            return inOrderTraverse(root.left)+[root.val]+inOrderTraverse(root.right)

        return inOrderTraverse(root)[k-1]



#Time complexity: O(H+k) H is a tree height. This results in O(log⁡N + k) balanced tree and O#(N+k) for completely unbalanced tree with all the nodes in the left subtree.

#Space complexity: O(H). O(N) in the worst case of the skewed tree, O(log N) in the average case of the balanced tree.




