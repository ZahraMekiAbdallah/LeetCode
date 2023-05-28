class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        q = deque([(root, 0, 0)])
        res = []
        min_n, max_n = 0, 0
        while len(q) > 0:
            node, row, col = q.popleft()

            dic[col].append((node.val, row))
            
            min_n = min(min_n, col)
            max_n = max(max_n, col)
            if node.left: q.append([node.left, row+1, col+1])
            if node.right: q.append([node.right, row+1, col-1])
        

        # Sorted by col Desc
        sorted_dic = sorted(dic)[::-1]
        
        for key in sorted_dic:
          #Sorted by row Asc             
          res.append([val[0] for val in sorted(dic[key], key=lambda x: (x[1], x[0]))])

        return res
        
# Time: O(n) for BFS, O(n.log(n/k)) for sorting while k is width of tree so finally is O(n.logn)

# Time Complexity: O(n.logn)
# Space Compexity: O(n)
