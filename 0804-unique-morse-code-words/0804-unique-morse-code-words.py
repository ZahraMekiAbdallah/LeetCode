class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        base = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
        res = set()
    
        for word in words:
            st = ''
            for char in word:
                st += base[ord(char) - ord('a')]
            res.add(st)
        return len(res)
    
        