class Solution:
    def countPrimes(self, n):

        if n <= 2:
            return 0

        prime = [True] * n

        prime[0] = False
        prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):

            if prime[i]:

                for j in range(i * i, n, i):
                    prime[j] = False

        count = 0

        for i in range(n):
            if prime[i]:
                count += 1

        return count