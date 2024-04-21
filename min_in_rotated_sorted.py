class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            # find the midpoint 
            m = (l + r) // 2
            
            # Comps
            if m > 0 and nums[m] < nums[m-1]:
                return nums[m]
            
            # if after rotation point
            elif nums[m] < nums[-1]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]
            