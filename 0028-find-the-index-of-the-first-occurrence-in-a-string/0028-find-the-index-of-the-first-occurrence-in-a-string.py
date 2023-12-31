class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            n = 0
            if haystack[i] == needle[n]:
                j = i+1
                n += 1
                while j < len(haystack) and n < len(needle):
                    if haystack[j] == needle[n]:
                        j+=1
                        n+=1
                    else:
                        break
                
                if n == len(needle):
                    return i
        return -1
            