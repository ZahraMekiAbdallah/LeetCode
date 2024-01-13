
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        p1_count, p2_count = 0, 0
        mid = len(s)//2
        
        for i in range(len(s)):
            if s[i] in vowels:
                if i >= mid:
                    p2_count += 1
                else:
                    p1_count += 1

        return p1_count == p2_count
                    
    
    