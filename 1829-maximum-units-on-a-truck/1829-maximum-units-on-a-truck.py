class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Want smallest: number of box/unit ratio
        Need an ordered list of most units per box

        1. Get ordered list of indices based on the ratioo
        2. Iterate through those ordered indices
            a. Add boxes until you hit truck size
        """
        #Create ordered list
        n=len(boxTypes)
        
        ordered = sorted(boxTypes, key=lambda x:x[1], reverse=True)

        numUnits = 0

        for i in range(n):
            cur = ordered[i]
            box, unit = cur[0], cur[1]
            
            numBoxes = min(truckSize, box)
            truckSize -= numBoxes
            numUnits += numBoxes*unit
            if truckSize == 0:
                break

        return numUnits