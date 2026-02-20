class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = set(nums)
        target = set()

        for i in range(len(nums)+1):
            target.add(i)

        for elm in target:
            if elm not in cur:
                return elm


        

     