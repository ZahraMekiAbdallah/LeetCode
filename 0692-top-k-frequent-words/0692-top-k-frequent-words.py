from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      ''' sorted by the frequency then sort the words with the same frequency'''
      dic = Counter(words)
      dic_vals = defaultdict(list)
      
      for key, val in dic.items():
        dic_vals[val].append(key)
      
      sorted_dic_vals = sorted(dic_vals.items(), key=lambda x:x[0], reverse=True)
  
      flat_sorted_lst = []
      for key, val in sorted_dic_vals:
        for item in sorted(val):
          flat_sorted_lst.append(item)
          
      res = []
      for item in flat_sorted_lst:
        res.append(item)
        k-=1
        if k == 0:
          break
          
      return res
        
        
      
      
      
        