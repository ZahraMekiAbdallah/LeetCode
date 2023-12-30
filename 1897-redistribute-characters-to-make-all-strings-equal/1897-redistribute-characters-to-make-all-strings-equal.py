import collections

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # O(n.m) as n=len(words), m=values in counter
        for val in collections.Counter(''.join(words)).values(): 
            if val % len(words) != 0:
                return False
            
        return True