# leetcode:43 Medium
# Ikkita string tipdagi sonni integer tipga o'zgartirmasdan ko'paytirish kerak

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0", 0

        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)

        for i in range(n2 - 1, -1, -1):
            carry = 0
            for j in range(n1 - 1, -1, -1):
                temp = int(num2[i]) * int(num1[j]) + carry + result[i + j + 1]
                carry, result[i + j + 1] = divmod(temp, 10)
            result[i + j] += carry

        res_1 = ""
        res_2 = 0
        len_result = len(result)
        for i in range(len_result):
            if not (result[i] == 0 and not res_1):
                res_1 += str(result[i])
                res_2 += result[i] * 10**(len_result - i - 1)

        return res_1, res_2


solution = Solution()
result = solution.multiply(num1="15", num2="2")

print("result=", result)
