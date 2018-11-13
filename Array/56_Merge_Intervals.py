"""合并所有相交的子数组

思路：先按首元素排序，然后逐步合并，注意完全被包含的子数组，因此要判断合并后end的变化

Returns:
    [type] -- [description]
"""


import unittest

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x:x.start)
        result = []
        result.append(intervals[0])

        for index in range(1, len(intervals)):
            if intervals[index].start <= result[-1].end:
                if intervals[index].end > result[-1].end:
                    result[-1].end = intervals[index].end
            else:
                result.append(intervals[index])

        return result