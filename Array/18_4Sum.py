import unittest


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import Counter
        
        counter = Counter(nums)
        keys = list(counter.keys())
        keys.sort()
        result = []
        
        length = len(keys)

        for i in range(length):
            print(i,keys[i],keys[i]>target)
            if keys[i] > target:
                break
            counter[i] -= 1
            for j in range(length - 1, i-1, -1):
                if keys[j] < target:
                    break
                counter[j] -= 1
                temp_target = target - keys[i] - keys[j]
                p = i if counter[i] > 0 else i + 1
                q = j if counter[j] > 0 else j - 1
                print(keys[i], keys[j])
                while p <= q:
                    sum_ = keys[p] + keys[q]
                    if sum_ == temp_target:
                        if p == q and counter[p] == 1:
                            break
                        result.append([keys[i], keys[p], keys[q], keys[j]])
                        p += 1
                    elif sum_ < temp_target:
                        p += 1
                    else:
                        q -= 1

                counter[j] += 1
            counter[i] += 1

        return result
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 0, -1, 0, -2, 2]
        print(self.s.fourSum(input, 0))
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
