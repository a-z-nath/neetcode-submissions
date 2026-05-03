class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry:
                digit, carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
                res.append(digit)
            else:
                digit = digits[i]
                res.append(digit)
        if carry:
            res.append(carry)
        return res[::-1]