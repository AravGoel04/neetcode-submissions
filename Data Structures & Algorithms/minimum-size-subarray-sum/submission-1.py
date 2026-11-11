class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sums = 0
        length = len(nums) + 1

        for i in range(len(nums)):
            sums += nums[i]

            while sums >= target:
                current_length = i - l + 1
                length = min(length, current_length)

                sums -= nums[l]
                l += 1

        if length == len(nums) + 1:
            return 0

        return length


                



