class Solution:
    def isSame(self, a, b) -> bool:
        return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]

    def isGreater(self, a, b) -> bool:
        return a[0] > b[0] or a[1] > b[1] or a[2] > b[2]

    def merge(self, a, b):
        return (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2]))

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        run_trip = triplets[0]
        n = len(triplets)

        for i in range(1, n):
            if self.isSame(run_trip, target):
                return True

            nxt = self.merge(run_trip, triplets[i])

            if self.isGreater(nxt, target):
                if self.isGreater(run_trip, target):
                    run_trip = triplets[i]
                continue

            run_trip = nxt

        return self.isSame(run_trip, target) 