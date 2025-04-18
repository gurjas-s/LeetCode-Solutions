class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        #row index is the count, columns are the nums
        #this is bucket sorting
        arr = [[] for i in range(n+1)] 
        highest = float("-inf")
        for num, count in freq.items():
            highest = max(highest, count) #index for k=1
            arr[count].append(num)
        
        res = []
        for i in range(highest, highest-k-1, -1):
            for j in range(len(arr[i])):
                if arr[i][j] != float("-inf"):
                    res.append(arr[i][j])
                    if len(res) == k:
                        return res
                
        return res