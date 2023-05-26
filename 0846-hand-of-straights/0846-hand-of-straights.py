from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
      '''  consecutive cards '''
      
      if len(hand) % groupSize > 0:
        return False
      
      dic = Counter(hand)
      
      for k in sorted(dic): 
        while dic[k] > 0:
          for i in range(k, k+groupSize): # ** for each number check is group will be consecutive **
            if dic.get(i) and dic[i] - 1 >= 0:
              dic[i] -= 1
            else:
              return False
          
      return True
        
        
          
      