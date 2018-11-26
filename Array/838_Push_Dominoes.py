import unittest


class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        dominoes = [s for s in dominoes]
        length = len(dominoes)

        if length < 2:
            return ''.join(dominoes)

        change = True
        while change:
            change = False
            temp_s = dominoes[:]

            if dominoes[0] == '.' and dominoes[1] == 'L':
                temp_s[0] = 'L'
            
            if dominoes[-1] == '.' and dominoes[-2] == 'R':
                temp_s[-1] = 'R'

            for i in range(1, length - 1):
                if dominoes[i] == '.':
                    if dominoes[i-1] == 'R' and dominoes[i+1] != 'L':
                        change = True
                        temp_s[i] = 'R'
                    elif dominoes[i+1] == 'L' and dominoes[i-1] != 'R':
                        change = True
                        temp_s[i] = 'L'
            dominoes = temp_s
        
        return ''.join(dominoes)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = ".L.R...LR..L.."
        self.assertEqual(self.s.pushDominoes(input), "LL.RR.LLRRLL..")
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
