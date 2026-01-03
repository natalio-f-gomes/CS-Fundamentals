class PigLatin:
    def __init__(self,text):
        self.text = text
    def GetPigLatin(self):
        vowels = "aeiouAEIOU"
        new_word = ""
        for i in self.text:
            if i in vowels:
                new_word = self.text[self.text.index(i):]+ self.text[:self.text.index(i)]+"ay"
                break
                
        return new_word


