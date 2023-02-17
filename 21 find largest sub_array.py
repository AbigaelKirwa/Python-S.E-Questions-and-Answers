# from math import inf
# def maxSubArray(nums):
#     ans = -inf
#     for i in range(len(nums)):
#         cur_sum = 0
#         for j in range(i, len(nums)):
#             cur_sum += nums[j]
#             ans = max(ans, cur_sum)
#     return ans

# nums = [1,2,3,4,5,6]
# print("the largest sub array sum is", maxSubArray(nums))

from math import inf

def maxSubArray(nums):
    ans = -inf

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(len(nums)):
            curr_sum += nums[j]
            ans = max(ans, curr_sum)
    return ans

nums = [-1,2,3,4,5,6]
print("the largest sub array sum is", maxSubArray(nums))