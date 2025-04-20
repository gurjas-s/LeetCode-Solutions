class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1]*n
        after = [1]*n

        product = 1
        for i in range(n):
            before[i] = product
            product *= nums[i]

        product = 1
    
        for i in range(n-1,-1,-1):
            after[i] = product
            product *= nums[i]
          
      
        res = [before[i]*after[i] for i in range(n)]
        return res