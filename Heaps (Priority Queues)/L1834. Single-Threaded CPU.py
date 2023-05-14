class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda a : a[0])
        
        res, heap = [], []
        i, time = 0, tasks[0][0]
        while heap or i<len(tasks):
            while i < len(tasks) and time >= tasks[i][0] :
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i+=1
                
            if heap:
                procTime, idx = heapq.heappop(heap)
                res.append(idx)
                time += procTime
            else:
                time = tasks[i][0]
                
        return res
 
        