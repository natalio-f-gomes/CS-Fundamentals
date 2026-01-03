class Vowel:
    def __init__(self, string_text):
        self.string_text = string_text
    def GetVowels(self):
        vouls = "aeiouAEIOU"
        count = 0
        for i in self.string_text:
            for j in vouls:
                if i==j:
                    count +=1

        return count
      
 from Vowel import *     
 
a = Vowel("Natalio")
print(a.GetVowels())
