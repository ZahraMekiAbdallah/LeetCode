from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        if len(set(dic.values())) == len(dic):
          return True
        return False