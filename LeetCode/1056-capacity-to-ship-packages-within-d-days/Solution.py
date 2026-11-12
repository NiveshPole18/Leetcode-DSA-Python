class Solution:
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left <= right:

            mid = (left + right) // 2

            total = 0
            count = 1

            for weight in weights:

                if total + weight <= mid:
                    total += weight

                else:
                    count += 1
                    total = weight

            if count <= days:
                right = mid - 1

            else:
                left = mid + 1

        return left