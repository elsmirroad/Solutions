from lc import *
# =================================================================================
# 3629. Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
# =================================================================================


MX = 10**6 + 10
sieve = [True] * MX
sieve[0], sieve[1] = False, False
spf = [0] * MX

for i in range(2, MX):
    if sieve[i]:
        spf[i] = i
        for j in range(i+i, MX, i):
            sieve[j] = False
            if spf[j] == 0: spf[j] = i


def get_factors(x):
    result = set()
    while x > 1:
        p = spf[x]
        result.add(p)
        x //= p
    return result


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        groups = defaultdict(list)

        for i, x in enumerate(nums):
            for p in get_factors(x):
                groups[p].append(i)

        q = deque([(0, 0)]) # idx, jumps
        seenPrimes, seenIdx = set(), set([0])

        while q:
            i, jumps = q.popleft()
            if i == n-1: return jumps

            if i + 1 < n and not i+1 in seenIdx:
                q.append((i+1, jumps+1))
                seenIdx.add(i+1)

            if 0 <= i - 1 and not i-1 in seenIdx:
                q.append((i-1, jumps+1))
                seenIdx.add(i-1)

            if nums[i] in groups and not nums[i] in seenPrimes:
                seenPrimes.add(nums[i])
                for j in groups[nums[i]]:
                    if not j in seenIdx:
                        q.append((j, jumps + 1))
                        seenIdx.add(j)


test("""
You are given an integer array nums of length n.
You start at index 0, and your goal is to reach index n - 1.
From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.

Return the minimum number of jumps required to reach index n - 1.
 
Example 1:

Input: nums = [1,2,4,6]
Output: 2
Explanation:
One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.

Thus, the answer is 2.

Example 2:

Input: nums = [2,3,4,7,9]
Output: 2
Explanation:
One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.

Thus, the answer is 2.

Example 3:

Input: nums = [4,6,5,8]
Output: 3
Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.


 
Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^6


""")
