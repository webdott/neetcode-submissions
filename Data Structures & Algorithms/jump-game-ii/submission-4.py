class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, n = 0, len(nums)

        if n == 1:
            return 0

        q = deque([0])
        seen = defaultdict(set)
        seen[0].add(0)

        while q:
            l = len(q)

            steps += 1

            # print(q, steps)

            for _ in range(l):
                h = q.popleft()

                if h + nums[h] >= n - 1:
                    return steps

                for j in range(h + len(seen[steps]) + 1, h + nums[h] + 1):
                    if j not in seen[steps - 1] and j not in seen[steps]:
                        q.append(j)
                        seen[steps].add(j)
                
        return steps

                