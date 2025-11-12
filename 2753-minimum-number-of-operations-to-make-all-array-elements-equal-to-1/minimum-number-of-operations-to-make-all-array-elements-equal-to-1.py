from math import gcd

class Solution:
    # Recursive helper to find shortest subarray that gives GCD = 1
    def gcdlen(self, nums, a, i):
        if a == 1:
            return 1  # Found subarray with GCD = 1
        if i == len(nums):
            return float('inf')  # Reached end without finding GCD = 1
        return 1 + self.gcdlen(nums, gcd(a, nums[i]), i + 1)  # Continue exploring

    def minOperations(self, nums):
        n = len(nums)
        flg = False  # Flag to check if any adjacent pair has GCD = 1
        oc = 1 if nums[0] == 1 else 0  # Count of 1s
        gc = nums[0]  # Initial GCD of array

        # Step 1: Compute global GCD and check for 1s or adjacent GCD=1 pairs
        for i in range(1, n):
            gc = gcd(gc, nums[i])  # Update overall GCD
            if gcd(nums[i], nums[i-1]) == 1:
                flg = True  # Found pair with GCD = 1
            if nums[i] == 1:
                oc += 1  # Count ones

        # Case 1: Already have a 1 or adjacent pair makes GCD = 1
        if flg:
            return n - oc

        # Case 2: If overall GCD never becomes 1, impossible
        if gc != 1:
            return -1

        # Step 2: Find shortest subarray with GCD = 1
        length = float('inf')
        for i in range(n - 1):
            length = min(length, self.gcdlen(nums, nums[i], i + 1))

        # Step 3: Spread the '1' through the array
        return int(length + n - 2)
        