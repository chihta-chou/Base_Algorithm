class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while True:
            q = self.partition(nums, l, r)
            if (q == n-k):
                return nums[q]
            elif q < n-k:
                l = q+1
            else:
                r = q-1

    def partition(self, arr, low, high):
        i, pivot = low-1, arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
