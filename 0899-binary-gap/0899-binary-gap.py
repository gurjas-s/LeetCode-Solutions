class Solution:
    def binaryGap(self, n: int) -> int:
        """
        1010101
        00101
        """
        l=0
        max_dist=0
        is_seen=False
        binary=str(bin(n))
        binary = binary[2:]
        #print(binary)
        for r in range(len(binary)):
            #print(binary[r])
            if binary[r] == "1":
                dist=r-l
                print(r)
                max_dist=max(max_dist,dist)
                l=r
    
        return max_dist