from heapq import heappush, heappop

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        def neighbors(lock):
            res = []
            for i in range(4):
                d = int(lock[i])
                for nd in [(d + 1) % 10, (d - 1) % 10]:
                    res.append(lock[:i] + str(nd) + lock[i+1:])
            return res

        def hamming(a, b):
            return sum(x != y for x, y in zip(a, b))

        pq = []
        heappush(pq, (hamming("0000", target), 0, "0000"))
        visited = set(["0000"])

        while pq:
            f, g, lock = heappop(pq)
            if lock == target:
                return g

            for nxt in neighbors(lock):
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    heappush(
                        pq,
                        (g + 1 + hamming(nxt, target), g + 1, nxt)
                    )

        return -1
