class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find first target then last target

        [5,6,7,7,8,8,10]
        [5,6,7,7]
        [5,6]
        """
        def find_left(nums):
            n=len(nums)
            r=n-1
            l=0
            while(l<r):
                m=(r+l)//2
                right, mid, left = nums[r], nums[m], nums[l]
                if nums[l] == target:
                    return l
                elif nums[m] >= target:
                    r=m
                elif nums[m] < target:
                    l=m+1
            if (l>=0 and l<n) and nums[l]==target:
                return l
            return -1
        def find_right(nums):
            n=len(nums)
            r=n-1
            l=0
            while(l<r):
                m=(r+l)//2
                right, mid, left = nums[r], nums[m], nums[l]             
                if nums[r] == target:
                    return r
                elif nums[m] == target:
                    if (r-m==1) and r<len(nums) and nums[m] == target:
                        return m
                    else:
                        l=m
                elif nums[m]>target:
                    r=m-1
                elif nums[m]<target:
                    l=m+1 
            if (r>=0 and r<n) and nums[r]==target:
                return r
            return -1

        left=find_left(nums)
        print(left)
        right=find_right(nums)
        print(right)
        return [left,right]