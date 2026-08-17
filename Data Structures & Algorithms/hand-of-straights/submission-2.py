class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        no_buckets = n // groupSize

        if n > groupSize * no_buckets:
            return False

        hand.sort()
        curr = 0
        s = defaultdict(int)
        b = defaultdict(list)

        for i, h in enumerate(hand):
            if not s[h - 1]:
                curr += 1
                b[h].append(1)
            else:
                s[h - 1] -= 1
                size = b[h - 1].pop()

                if size == groupSize - 1:
                    continue

                b[h].append(size + 1)

            s[h] += 1

            if curr > no_buckets:
                return False

        return True

    #  no buckets = total / group_size
    #  no previous number from group size: curr += 1
    #  if curr > no_buckets: return False
    #  End: return True