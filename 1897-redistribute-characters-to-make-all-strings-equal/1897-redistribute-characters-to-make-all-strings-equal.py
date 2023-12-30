import collections

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        for key, val in collections.Counter(''.join(words)).items():
            if int(val / len(words)) != val / len(words):
                return False
            
        return True