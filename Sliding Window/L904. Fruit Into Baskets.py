# there is another ay to solve the dictionary problem maintain a unique variable
# and whenever we are inside 2 while loop and key goes to 0 we can do unique-=1
# and whenever we hit s.t value==1 unique++.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict()
        i, j, maxi = 0, 0, -float("inf")
        while j<len(fruits):
            if fruits[j] in count:
                count[fruits[j]] += 1
            else:
                count[fruits[j]] = 1
            while len(count)>2:
                count[fruits[i]] -= 1
                if not count[fruits[i]]:
                    count.pop(fruits[i])
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi