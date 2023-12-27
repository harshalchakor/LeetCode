# 

class Answer:
    def wordPattern(self, pattern: str, text: str) -> bool:
        
        word = text.split(" ")
        
        if len(pattern) != len(word):
            return False
            
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, word):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
                
            charToWord[c] = w
            wordToChar[w] = c
            
        return True
       
        
ans = Answer()
print(ans.wordPattern("abba", "cat bat bat cat"))
print(ans.wordPattern("xxyx", "man women man women"))
print(ans.wordPattern("klm", "I love you"))
print(ans.wordPattern("pqpqr", "I love I love you"))
print(ans.wordPattern("hu", "who who"))



