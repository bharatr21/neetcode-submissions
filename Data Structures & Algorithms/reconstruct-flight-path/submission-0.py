class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        res = ["JFK"]
        for src, dst in tickets:
            adj[src].append(dst)
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            for idx, v in enumerate(adj[src]):
                adj[src].pop(idx)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(idx, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
