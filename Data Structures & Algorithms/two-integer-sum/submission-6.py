class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n          # what number do I need?
            if diff in prevMap:        # have I seen it before?
                return [prevMap[diff], i]   # return both indexes
            prevMap[n] = i             # if not, store current number