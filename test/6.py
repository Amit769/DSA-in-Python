class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next # craeted the linked list


class Solution: # start the solution
    def mergeKLists(self, lists):
        values = []

        for head in lists:
            while head:
                values.append(head.val)
                head = head.next # go through each linked list

        values.sort()

        dummy = ListNode() # create new linked list
        cur = dummy # cur add next node

        for x in values:
            cur.next = ListNode(x)
            cur = cur.next # create nodes one by one 

        return dummy.next  #return actual lsit 