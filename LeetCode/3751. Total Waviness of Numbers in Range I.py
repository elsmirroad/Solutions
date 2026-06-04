from lc import *
# ===================================================================
# 3751. Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# ===================================================================


class Solution:
    def totalWaviness(self, num1: int, num2: int, total=0) -> int:
        def func(num):
            if num < 100: return 0
            cnt = 0
            prePrev = num - (num//10) * 10
            num //= 10
            prev = num - (num//10) * 10
            num //= 10
            while num > 0:
                curr = num - (num//10) * 10
                num //= 10
                if (prev < curr and prev < prePrev) or (prev > curr and prev > prePrev): cnt += 1
                prePrev = prev
                prev = curr
            return cnt
        return sum(func(num) for num in range(num1, num2+1))


class Solution:
    def totalWaviness(self, num1: int, num2: int, total=0) -> int:
        for num in range(num1, num2+1):
            if num < 99: continue
            num = str(num)
            for i in range(1, len(num)-1):
                if num[i-1] < num[i] and num[i+1] < num[i]: total += 1
                elif num[i-1] > num[i] and num[i+1] > num[i]: total += 1
        return total


class Solution:
    def totalWaviness(self, num1: int, num2: int, total=0) -> int:
        return sum(a < b > c or a > b < c for num in map(str, range(num1, num2+1)) for a, b, c in zip(num, num[1:], num[2:]))


test("""
You are given two integers num1 and num2 representing an inclusive range [num1, num2].
The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range [num1, num2].
 
Example 1:

Input: num1 = 120, num2 = 130
Output: 3
Explanation:
In the range [120, 130]:


120: middle digit 2 is a peak, waviness = 1.
121: middle digit 2 is a peak, waviness = 1.
130: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202
Output: 3
Explanation:
In the range [198, 202]:


198: middle digit 9 is a peak, waviness = 1.
201: middle digit 0 is a valley, waviness = 1.
202: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848
Output: 2
Explanation:
Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 
Constraints:

1 <= num1 <= num2 <= 10^5


""")
