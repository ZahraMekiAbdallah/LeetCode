class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dic = {}
        l, r = 0, 0
        res = float('-inf')

        while l <= r and r < len(s):
            if s[r] not in dic:
                dic[s[r]] = 1
                if r - l + 1 > res:
                    res = r - l + 1
            else:
                dic[s[r]] += 1
                while dic.get(s[r]) > 1:
                    if dic.get(s[l]):
                        dic[s[l]] -= 1
                    l+=1

                if r - l + 1 > res:
                    res = r - l + 1
            r+=1

        return res if res != float('-inf') else 0




