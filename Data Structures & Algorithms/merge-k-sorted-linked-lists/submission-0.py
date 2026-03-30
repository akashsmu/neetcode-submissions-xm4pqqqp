# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                res.append(temp.val)
                temp = temp.next
        res.sort()
        dummy = ListNode(0)
        curr = dummy
        for num in res:
            node = ListNode(num)
            curr.next = node
            curr = curr.next
        return dummy.next

