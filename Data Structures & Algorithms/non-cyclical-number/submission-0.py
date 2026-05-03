class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfDigitsSquare(n)
        return True if n == 1 else False
        
    def sumOfDigitsSquare(self, n):
        output = 0
        while n != 0:
            digit = n % 10
            digit = digit ** 2
            n //= 10
            output += digit
        return output