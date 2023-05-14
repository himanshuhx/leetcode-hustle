'''
we need to find count of unique pairs whose diff is k
ex k = 2 [3,1,4,1,5]
here (3,5) (5,3) = 1 pair only 
      if k was 0 (1,1) (1,1) ans will be 1 
so pairs are (3,1) and (5,3) where diff = 2

first approach is using map
Time - O(N) Space O(1)
we will store the count of frequency of each num in map
so map we look like { 1:2,
                      3:1,
                      4:6,
                      5:1 }
        {now if k==0 than we know only those pair will exist whose occurence is > 1
        for ex [1,1,2,2] k =1 here (1,1) and (2,2) only two pairs are possible }
        we will iterate in map and check if ele + k ids present in ma if yes ans++ 
        ex - 2(k)+1 is in map? yes 3 is in map.. ans++
             2(k)+3 is in map? yes 5 is in map...ans+++
             likewise...
        return ans

Binary Search
Time Complexity - O(nlogn)
Space Complexity - O(1)

sort the array 
iterate over array
do a binary search is nums[i]+k in nums?
if yes append it to a set
why set? because we want unique pairs only

'''  
def findPairs(nums, k) -> int:
        if k<0:
            return 0
        res = 0
        map = {}
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
        for ele in map:
            if k==0:
                if map[ele]>1:
                    res+=1
            else:
                if ele+k in map:
                    res+=1
        return res