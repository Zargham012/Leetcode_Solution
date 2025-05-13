class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        Abc= 0
        while Abc<len(nums):
            if nums[Abc] == val:
                nums.pop(Abc)
            else:
                Abc +=1
        return len(nums)

