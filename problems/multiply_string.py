# Ikkita string tipdagi sonni integer tipga o'zgartirmasdan ko'paytirish kerak

class Solution(object):
    def multiply(self, num1, num2):
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)

        for i in range(n2 - 1, -1, -1):
            carry = 0
            for j in range(n1 - 1, -1, -1):
                temp = int(num2[i]) * int(num1[j]) + carry + result[i + j + 1]
                carry, result[i + j + 1] = divmod(temp, 10)
                print(carry, result)

        return result


solution = Solution()
result = solution.multiply(num1="5", num2="15")

print("result=", result)
