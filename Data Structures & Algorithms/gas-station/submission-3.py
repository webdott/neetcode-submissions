class Solution:
    def canCompleteCircuitA(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            g = gas[i]
            c = cost[i]

            if g < c:
                continue

            g -= c
            j = (i + 1) % n

            while j != i:
                g += gas[j]

                if g < cost[j]:
                    break

                g -= cost[j]
                j = (j + 1) % n

            if j == i:
                return i

        return -1
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        res = 0
        g, t = 0, 0

        for i in range(n):
            g += (gas[i] - cost[i])
            t += (gas[i] - cost[i])

            if g < 0:
                g = 0
                res = i + 1
            
        return res if t >= 0 else -1