"""
思路：利用最小堆的特性，来使得每次节点变化时，能够进行快速排序
"""

import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

       
        smallest_heap = []
        for index,list_ in enumerate(lists):
            if list_ is not None:
                heapq.heappush(smallest_heap, (list_.val, index)) # 利用值和index进行稳定排序
        
        head_ptr = ListNode(0)
        ptr = head_ptr

        while smallest_heap:
            _,index = heapq.heappop(smallest_heap)

            ptr.next = lists[index]
            ptr = ptr.next
            lists[index] = lists[index].next
            ptr.next = None
            
            if lists[index] is not None:
                heapq.heappush(smallest_heap, (lists[index].val, index))

        return head_ptr.next

