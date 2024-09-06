# leetcode: 35 Easy
# Search Insert Position - List ichida maqsadimiz index ini topish, agar yoq bo'lsa o'rni indexsini qaytarish
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


data = Solution()
result = data.searchInsert(nums=[1, 3, 5, 6], target=7)

print("result=", result)
