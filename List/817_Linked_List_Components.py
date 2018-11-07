"""寻找列表中的组件

思路：
1. 我的思路过于复杂，先把链表放到hash中，然后利用标记来处理
2. 直接把Group set化，这样搜查起来的会快

Returns:
    [type] -- [description]
"""


from utils import *
import unittest


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        p = head
        next_map = {}
        while p:
            if p.next:
                next_map[p.val] = {'next' : p.next.val, 'visited':False, 'component':False}
            else:
                next_map[p.val] = {'next': None, 'visited': False, 'component':False}
            p = p.next
        
        cnt = 0

        for num in G:
            if num in next_map:
                next_map[num]['component'] = True

        from pprint import pprint
        pprint(next_map)

        for key,value in next_map.items():
            if value['component'] is False:
                continue
            else:
                if value['visited']:
                    continue
                flag = False
                p = key
                while p is not None:
                    if next_map[p]['component'] is False:
                        break
                    if next_map[p]['visited']:
                        flag = True
                        break

                    next_map[p]['visited'] = True
                    p = next_map[p]['next']

                if flag is False:
                    cnt += 1
        return cnt
                
class TestComponent(TestList):

    def test_one(self):
        head = self.make_list([4,3,1,2,0])
        s = Solution()
        cnt = s.numComponents(head, [1,3,0])

        print(cnt)

if __name__ == "__main__":
    unittest.main()