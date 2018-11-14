import unittest


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        import collections

        meet = collections.defaultdict(list)

        for word in words:
            meet[word[0]].append(iter(word[1:]))

        for s in S:
            values = meet.pop(s, None)

            if values:
                for value in values:
                    meet[next(value, None)].append(value)

        return len(meet[None])
            
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        S = "abcde"
        words = ["a", "bb", "acd", "ace"]

        self.assertEqual(self.s.numMatchingSubseq(S,words), 3)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
