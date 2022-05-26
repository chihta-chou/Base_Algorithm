

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        total = 0
        res = 1
        for r in range(1, n):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        ans = []
        a, b, c = 0, 0, 0
        for i in range(l-2):
            total = nums[i]
            if total > 0:
                return []
            for j in range(i+1, l-1):
                total += nums[j]
                if total > 0:
                    return []
                for k in range(j+1, l):
                    total += nums[k]
                    if total > 0:
                        break
                    elif total == 0:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans
