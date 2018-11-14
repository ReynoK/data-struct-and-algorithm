class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        h = len(numbers) - 1

        while True:
            sum_ = numbers[l] + numbers[h]
            if sum_ == target:
                return [l+1,h+1]

            if sum_ < target:
                l += 1
            else:
                h -= 1

        