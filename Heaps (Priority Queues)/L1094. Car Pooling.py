class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = sorted([(trip[1], trip[0]) for trip in trips])
        end = sorted([(trip[2], trip[0]) for trip in trips])

        curr = maxi = 0
        i, j = 0, 0

        while i < len(start):
            if start[i][0] < end[j][0]:
                curr += start[i][1]
                i += 1
            else:
                curr -= end[j][1]
                j += 1

            maxi = max(maxi, curr)

        return maxi <= capacity


# meeting room ii
