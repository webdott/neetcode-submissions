class Solution:
    def factorial(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return n * self.factorial(n - 1)

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        r = n - 1

        total_len = self.factorial(n) / self.factorial(n - r)

        q, ans = deque([nums]), []
        seen = set()

        while q:
            m = len(q)

            if len(ans) + m == total_len:
                ans += q
                break;

            for i in range(m):
                curr_iter = q.popleft()

                ans.append(curr_iter)
                seen.add(tuple(curr_iter))

                for j in range(len(curr_iter)):
                    l = [curr_iter[j]]

                    for k in range(len(curr_iter)):
                        if j == k:
                            continue

                        l.append(curr_iter[k])
                    
                    t = tuple(l)

                    if t not in seen:
                        seen.add(t)
                        q.append(l)

        return ans