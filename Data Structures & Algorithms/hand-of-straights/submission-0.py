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
    #  if duplicate / no previous number: curr += 1
    #       seen: no - no of occurences
    #       3: 1, 7: 1

    #       5: 1  -> 2
    #  if curr > no_buckets: return False
    #  return True