# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
    

'''
Time Complexity: O(n) where n is the number of nodes in the linked list.
We traverse the linked list once to find the middle node.

Space Complexity: O(1) as we are using a constant amount of extra space for the pointers 
(slow, fast, prev) and not using any additional data structures.
'''