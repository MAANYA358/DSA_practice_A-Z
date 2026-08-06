class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:

            product = 1
            num = n

            # Calculate product of digits
            while num > 0:
                digit = num % 10
                product *= digit
                num //= 10

            # Check divisibility
            if product % t == 0:
                return n

            n += 1
