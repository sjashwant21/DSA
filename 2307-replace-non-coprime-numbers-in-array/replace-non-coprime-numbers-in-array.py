from math import gcd
from typing import List

class Solution:
    # Helper function to calculate LCM
    def lcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return a * b // gcd(a, b)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # Keep merging the last two elements as long as they are non-coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.lcm(a, b))
        
        return stack