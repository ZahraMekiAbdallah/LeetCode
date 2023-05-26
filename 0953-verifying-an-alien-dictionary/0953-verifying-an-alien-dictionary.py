class Solution:
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
      dic = {}
      for i in range(len(order)):
        dic[order[i]] = i
              
      for i in range(len(words)-1):
        for j in range(len(words[i])):
          if j >= len(words[i+1]): # first word larger than the second "apple, app"
            return False
          
          if dic[words[i][j]] != dic[words[i+1][j]] and dic[words[i][j]] > dic[words[i+1][j]]:
            return False
          
          if dic[words[i][j]] != dic[words[i+1][j]] and dic[words[i][j]] < dic[words[i+1][j]]:
            break # check the first difference letter if before the second one in second word
            
          
      return True
        