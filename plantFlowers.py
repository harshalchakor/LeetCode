# Plant[1] the given number of flowers when there is no adjecent flowers[0] in flowerbed.

class Answer:
    def plantFlowers(self, flowerbed, flowers) -> bool:
        
        # Add "0" tp left and right of the array to cover the edge case
        
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):              #skipping those first and last "0"skipping
            if flowerbed[i - 1] == flowerbed[i] == flowerbed [i + 1] == 0:
                flowerbed[i] = 1
                flowers -= 1
        return False if flowers else True
        

ans = Answer()
print(ans.plantFlowers([1, 0, 1, 0 ,1], 1))
print(ans.plantFlowers([1, 0, 0, 0 ,1], 1))
print(ans.plantFlowers([0, 0, 1, 0 ,0], 2))
print(ans.plantFlowers([1, 0, 1, 0 ,0], 1))
print(ans.plantFlowers([0, 1, 1, 1 ,0], 1))

        
