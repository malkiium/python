class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_List = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    num_List.append(i)
                    num_List.append(j)
                    return num_List
    


s = Solution()

def test(nums, target, expected):
    result = s.twoSum(nums, target)
    if result == expected:
        print(f"PASS ✅ | nums={nums}, target={target} -> {result}")
    else:
        print(f"FAIL ❌ | nums={nums}, target={target} -> got {result}, expected {expected}")

# Tests LeetCode
test([2,7,11,15], 9, [0,1])
test([3,2,4], 6, [1,2])
test([3,3], 6, [0,1])
