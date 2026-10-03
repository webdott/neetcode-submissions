class Solution:
    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:
        adj = {s: [] for s, d in tickets}

        tickets.sort()
        for s, d in tickets:
            adj[s].append(d)

        res = []
        def dfs(place):
            res.append(place)
            if len(res) == len(tickets) + 1: return True
            if place not in adj: 
                res.pop()
                return False

            temp = list(adj[place])
            for i, v in enumerate(temp):
                adj[place].pop(i)
                if dfs(v): return True
                adj[place].insert(i, v)

            res.pop()
            return False

        dfs("JFK")
        return res

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {s: [] for s, d in tickets}

        tickets.sort(reverse=True)
        for s, d in tickets:
            adj[s].append(d)

        res = []
        def dfs(place):
            if place not in adj or not adj[place]:
                res.append(place)
                return True

            while adj[place]:
                dfs(adj[place].pop())
            
            res.append(place)
            return True

        dfs("JFK")
        res.reverse()
        return res