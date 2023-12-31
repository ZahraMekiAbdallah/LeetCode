from collections import defaultdict 

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
            
        max_len = -1    
        for k, v in dic.items():
            max_len = max(max_len, v[-1] - v[0] - 1)
            
        return max_len