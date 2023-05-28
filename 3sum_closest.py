from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = []
        for k in range(n):
            i = k + 1
            j = n - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    return target
                l.append(s)
        abs_list = [abs(i - target) for i in l]
        return l[abs_list.index(min(abs_list))] # [1,2,5,10,11]l[abs_list.index(min(abs_list))]

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-100,-98,-2,-1], -101))