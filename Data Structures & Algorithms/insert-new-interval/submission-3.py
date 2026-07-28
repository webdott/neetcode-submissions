class Solution:
    def isOverlapping(self, a, b, c, d) -> bool:
        return (b <= d and c <= b) or (d <= b and a <= d)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
            
        ans, seen = [intervals[0]], False

        for a, b in intervals:
            c, d = ans[-1]

            if self.isOverlapping(a, b, c, d):
                ans[-1] = [min(a, c), max(b, d)]
            else:
                ans.append([a, b])

            e, f = ans[-1]

            # print(ans, a, b)

            if not seen:
                g, h = newInterval
                
                if self.isOverlapping(e, f, g, h):
                    ans[-1] = [min(e, g), max(f, h)]
                    seen = True
                elif h < e:
                    t = ans.pop()
                    ans.append([g, h])
                    ans.append(t)
                    seen = True

        if not seen:
            ans.append(newInterval)
            
        return ans


        