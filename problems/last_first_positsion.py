# leetcode: 34 Medium
# masivdagi maqsad elementlari boshi va oxirgisini indexini qaytarish, bo'lmasa [-1, -1] qaytarish kerak


class Solution(object):
    def searchRange(self, nums, target):
        # example 1
        result = self.find_with_for(nums, target)

        # example 2
        start = self.find_start(nums, target)
        end = self.find_end(nums, target)
        return [start, end]

    def find_with_for(self, nums, target):
        if target not in nums:
            return [-1, -1]

        start = 0
        end = 0
        first = False
        for i in range(len(nums)):
            if nums[i] == target and not first:
                first = True
                start = i
            elif nums[i] == target and first:
                end = i
        end = end if end > start else start

        return [start, end]

    def find_start(self, nums, target):
        start = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                start = mid

        return start

    def find_end(self, nums, target):
        end = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                end = mid

        return end


data = Solution()
result = data.searchRange(nums=[1, 3, 5, 6, 7, 7, 8, 8, 10, 10], target=7)

print("result=", result)
