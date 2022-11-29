# -*- coding: utf-8 -*-

import LinkedList from linkedlist.py

"""Merge Sort"""

class Solution(LinkedList):
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    # 归并法
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        pre = head
        slow = head               # 使用快慢指针来确定中点
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        left = head  
        right = pre.next  
        pre.next = None           # 从中间打断链表
        left = self.sortList(left)  
        right = self.sortList(right)  
        return self.merge(left,right)
        
    def merge(self, left, right):
        pre = LinkedList.Node(-1)
        first = pre
        while left and right:
            if left.value < right.value:
                pre.next = left
                pre = left
                left = left.next
            else:
                pre.next = right
                pre = right
                right = right.next
        if left:
            pre.next = left
        else:
            pre.next = right
                
        return first.next

    def printList(self,head):
        temp = self.sortList(head)
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print() 