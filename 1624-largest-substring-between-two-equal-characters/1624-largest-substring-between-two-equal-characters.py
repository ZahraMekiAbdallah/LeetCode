class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1   
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic:
                max_len = max(max_len, i - dic[s[i]] - 1)
            else:
                dic[s[i]] = i
            
        return max_len