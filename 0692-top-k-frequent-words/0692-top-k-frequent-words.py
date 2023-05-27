from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      ''' sorted by the frequency then sort the words with the same frequency'''
      dic = Counter(words)
      
      sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0])) # sort counter desc then words ascend
            
      return [item[0] for item in sorted_dic[:k]]
                
        