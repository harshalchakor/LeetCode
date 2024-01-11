# Reverse integer on 32bit scale.
class Answer():
    def reverseBit(self, n):
        
        res = 0
        
        for i in range(31):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        
        return res
        
                
ans = Answer()
print(ans.reverseBit(0))
print(ans.reverseBit(3))
print(ans.reverseBit(1)) # if you reverse it it's going to be 2^31 value.
print(ans.reverseBit(2147483648)) # if you reverse it, it's going to be 0 value.
