class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfDigitsSquare(n)
        while slow != fast:
            slow = self.sumOfDigitsSquare(slow)
            fast = self.sumOfDigitsSquare(self.sumOfDigitsSquare(fast))
        
        return True if fast == 1 else False
        
    def sumOfDigitsSquare(self, n):
        output = 0
        while n != 0:
            digit = n % 10
            digit = digit ** 2
            n //= 10
            output += digit
        return output