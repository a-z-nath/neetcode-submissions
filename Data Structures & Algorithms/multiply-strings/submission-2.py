class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        pos = 0
        res = "0"
        for i in range(l2-1, -1, -1):
            prod = self.mul(num1, num2[i], pos)
            res = self.addition(res, prod)
            pos += 1
        return res

    def mul(self, num: str, digit: str, pos: int) -> str:
        if num == "0" or digit == "0":
            return "0"
        res = []
        y = int(digit)
        carry = 0
        for i in range(len(num)-1, -1, -1):
            x = int(num[i])
            prod = (x * y) + carry
            res.append(str(prod % 10))
            carry = prod // 10
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1]) + "0" * pos

    
    def addition(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        res = []
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i>= 0 else 0
            y = int(num2[j]) if j>= 0 else 0
            add = x + y + carry
            res.append(str(add % 10))
            carry = add // 10
            i -= 1
            j -= 1
        return "".join(res[::-1])