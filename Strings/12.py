class Solution:
    def intToRoman(self, num: int) -> str:
     values = [
         (1000, "M"),
         (900, "CM"),
         (500, "D"),
         (400, "C"),
         (100, "XC"),
         (90, "XC"),
         (50, "XL"),
     ]
     
     result = ""
     
     for values, symbol in values:
         while num >= values:
             num -= value 
             
    return result         