class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            print(hashMap)
            print(n)
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return