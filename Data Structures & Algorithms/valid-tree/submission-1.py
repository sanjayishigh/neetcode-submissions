class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(x,y):
            px, py = find(x), find(y)

            if px == py:
                return False

            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]

            return True

        count = n
        for u,v in edges:
            if not union(u,v):
                return False
            count -= 1

        return count == 1