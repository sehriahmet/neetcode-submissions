class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        digits[-1] += 1
        for i in range(0, l):
            new_i = l - i - 1 
            if digits[new_i] >= 10:
                digits[new_i] = digits[new_i] % 10 
                if new_i == 0:
                    digits.insert(0, 1)
                else: digits[new_i-1] += 1

        return digits