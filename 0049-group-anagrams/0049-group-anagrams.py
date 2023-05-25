from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dic = defaultdict(list)
      res = []
      for i in range(len(strs)):
        key = tuple(sorted(Counter(strs[i]).items()))
        dic[key].append(strs[i])
      
      for k, v in dic.items():
        res.append(v)
        
      return res
        
# Time O(n*k) len of list * longest length of word 
# same for space