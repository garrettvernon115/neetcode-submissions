class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums: # traverse through nums
            if n in seen:
                return True
            seen.add(n)
        return False
        


                


        
