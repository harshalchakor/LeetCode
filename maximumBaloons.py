# How many maximum ballons from the given text you can spell? 

import collections

class Answer:
    def maximumBaloons(self, text) -> int:
        
        # create two hashmaps one for text and other balloon string itself and device the values.
        
        countText = {}
        balloon = {}
        
        for c in text:
            countText[c] = 1 + countText.get(c, 0)
        for c in "balloon":
            balloon[c] = 1 + balloon.get(c, 0)
        
        # countText = collections.Counter(text)
        # balloon = collections.Counter("balloon")
        
        res = len(text)
        
        for char in balloon:
            res = min(res, countText.get(char, 0) // balloon[char])
            # res = min(res, countText[char] // balloon[char])
            
        return res
        
        
ans = Answer()
print(ans.maximumBaloons("balloon"))
print(ans.maximumBaloons("balloon xyzballoon"))
print(ans.maximumBaloons("lobaballobbb"))
print(ans.maximumBaloons("balloonoon loonbalball "))
print(ans.maximumBaloons(""))
