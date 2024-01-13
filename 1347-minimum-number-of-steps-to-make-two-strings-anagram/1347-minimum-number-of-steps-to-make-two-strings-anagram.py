from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        diff_counter = 0
        
        for k,v in s_counter.items():
            if k in t_counter:
                if t_counter[k] < v:
                    diff_counter += (v - t_counter[k])
            else:
                diff_counter += v
            
        return diff_counter 
        
        
        
