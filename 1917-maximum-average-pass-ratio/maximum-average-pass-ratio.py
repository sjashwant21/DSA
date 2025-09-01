import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper function to compute gain
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        # Max-heap (store as negative because Python has min-heap by default)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        # Assign extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        # Calculate final average
        total = sum(p / t for _, p, t in heap)
        return total / len(classes)