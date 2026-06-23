class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for idx in range(len(nums)):
            compliment = target - nums[idx]

            if compliment in count:
                return [count[compliment], idx]

            count[nums[idx]] = idx

        return []