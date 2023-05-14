import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def solve():
            count = 0
            for tile in letter_count:
                if not letter_count[tile]:
                    continue
                letter_count[tile]-=1
                count += 1 + solve()
                letter_count[tile] += 1
            return count
            
            
        letter_count = collections.Counter(tiles)
        return solve()