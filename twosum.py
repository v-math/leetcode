#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : v-math
# @Description: 两个数之和.
# @Time     : 2023/2/15 22:13
# @File     : twosum.py
# @Project  : leetcode
from typing import List

"""
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i + 1:]):
                if num_i + num_j == target:
                    return [i, j + i + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
