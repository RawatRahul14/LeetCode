class Solution:
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            j = - i - 1
            num = num + digits[j] * 10**i
        num = str(num + 1)
        new_lst = []
        for i in range(len(num)):
            new_lst.append(int(num[i]))
        return new_lst