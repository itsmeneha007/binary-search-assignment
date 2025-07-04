bad = 4

def isBadVersion(version):
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

sol = Solution()
print(sol.firstBadVersion(5))  
