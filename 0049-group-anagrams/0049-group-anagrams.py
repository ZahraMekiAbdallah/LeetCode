from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dic = defaultdict(list)
      res = []
      for i in range(len(strs)):
        key = [0] * 26 
        for l in strs[i]:
          key[ord(l) - ord('a')] += 1
        dic[tuple(key)].append(strs[i]) 
        
      for k, v in dic.items():
        res.append(v)
        
      return res
        
# Time O(n*k) len of list * longest length of word 
# same for space