class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(p, s) for p, s in zip(position, speed)]
        position_speed.sort(reverse=True)
        stack = []

        for p, s in position_speed:
            secs = (target - p) / s

            if not stack or secs > stack[-1]:
                stack.append(secs)

        return len(stack)