class Solution:
    def findJudge(self, n, trust):

        trusted = [0] * (n + 1)

        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for person in range(1, n + 1):
            if trusted[person] == n - 1:
                return person

        return -1