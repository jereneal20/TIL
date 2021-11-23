class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groups = []
        start = 0
        for card in hand:
            for i in range(start, len(hand)):
                if len(groups) == i:
                    groups.append([])
                    groups[i].append(card)
                    break

                if groups[i][-1] + 1 == card:
                    if len(groups[i]) < groupSize:
                        groups[i].append(card)
                        break
                    else:
                        continue
                if groups[i][-1] == card:
                    continue
                if groups[i][-1] + 1 < card:
                    start += 1
                    continue

        for group in groups:
            if len(group) != groupSize:
                return False
        return True