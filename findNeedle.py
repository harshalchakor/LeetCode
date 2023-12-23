# Find the needle string in haystack string and retun the index of first occurance.

class Answer:
    def findNeedle(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) + 1 - len(needle)):  # go through every char of haystack untill it reaches len(needle)
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

ans = Answer()
print(ans.findNeedle("My name is Harshal Chakor", "Chakor"))
print(ans.findNeedle("Tough times never last but tough people do", "tough"))
print(ans.findNeedle("whats your name?", ""))
print(ans.findNeedle("showcase your art", "me"))


        
