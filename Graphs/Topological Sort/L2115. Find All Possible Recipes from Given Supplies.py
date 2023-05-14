class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)

        g = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(n):
            for ing in ingredients[i]:
                indegree[recipes[i]] += 1
                g[ing].append(recipes[i])

        q = deque(supplies)

        while q:
            curr = q.popleft()
            for nei in g[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = []

        for rec in recipes:
            if indegree[rec] == 0:
                res.append(rec)

        return res
