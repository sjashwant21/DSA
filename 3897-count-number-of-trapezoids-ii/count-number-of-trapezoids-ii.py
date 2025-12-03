class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        seen_points = []
        
        parallel_count = defaultdict(int)        # key: k (slope)
        same_line_count = defaultdict(int)       # key: (k, b) (slope, intercept)
        
        parallel_side_count = defaultdict(int)   # key: (k, side_length)
        same_line_side_count = defaultdict(int)  # key: (k, b, side_length)
        
        result = 0
        rhombus_twice = 0  
        
        for x1, y1 in points:
            for x2, y2 in seen_points:
                dx = x1 - x2
                dy = y1 - y2
                
                # Compute slope k
                if dx == 0:
                    k = "inf"
                    b = x1
                else:
                    k = dy / dx
                    b = y1 - k * x1
                    
                    # Round to avoid float precision issues
                    k = round(k, 8)
                    b = round(b, 8)
                
                slope_id = k
                line_id = (k, b)
                
                result += parallel_count[slope_id] - same_line_count[line_id]
                
                # Update counts
                parallel_count[slope_id] += 1
                same_line_count[line_id] += 1
                
                side_len = dx * dx + dy * dy   # squared length
                
                rhombus_twice += (
                    parallel_side_count[(k, side_len)]
                    - same_line_side_count[(k, b, side_len)]
                )
                
                parallel_side_count[(k, side_len)] += 1
                same_line_side_count[(k, b, side_len)] += 1
            
            seen_points.append((x1, y1))
        
        return result - rhombus_twice // 2