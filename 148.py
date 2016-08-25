# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution(object):

    def sortList(self, head):

        """

        :type head: ListNode

        :rtype: ListNode

        """

        if head == None:

            return None

        if head.next == None:

            return head

        slow = head

        fast = head

        while fast.next != None and fast.next.next != None:

            slow = slow.next

            fast = fast.next.next



        right = slow.next

        slow.next = None          

        left = head

        

        head = self.mergeLists(self.sortList(left), self.sortList(right))

        return head

        

    def mergeLists(self, l, r):

        res_head = ListNode(0)

        node = res_head

        while l != None and r != None:

            if l.val < r.val:

                node.next = l

                l = l.next

                node = node.next

            elif r.val <= l.val:

                node.next = r

                r = r.next

                node = node.next

        

        node.next = r if l == None else l

        return res_head.next

        





         

         

         

         

        

        
