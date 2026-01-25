class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def calculate_slope(points1:tuple, points2:tuple)->float:

            """
            slope_1 = (3-1)/(2-1) = 2
            slope_2 = (2-3)/(3-2) = -1
            """


            y2,x2 = points2
            y1,x1 = points1 
            denominator = x2 - x1
            numerator = y2 - y1
            if denominator == 0:
                return float("inf")
            return numerator/denominator

        slope_1 = calculate_slope(points[0], points[1])
        slope_2 = calculate_slope(points[1], points[2])
        
        for i in range(3):
            for j in range(3):
                if i!=j and points[i]==points[j]:
                    return False
        return slope_1!=slope_2
