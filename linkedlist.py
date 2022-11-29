class LinkedList(object):
    # Node class representing elements of linked list.
    class Node:
        def __init__(self, v, n=None):
            self.value = v
            self.next = n
            
    # Constructor of linked list.
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    def addHead(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def addTail(self, value):
        newNode = self.Node(value, None)
        curr = self.head
        if self.head == None:
            self.head = newNode
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        self.size += 1

    def length(self):
        return self.size
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print()    
    
    def deleteNode(self, delValue):
        #delete Information
        temp = self.head
        if self.isEmpty():
            return False
        if delValue == self.head.value:
            self.head = self.head.next
            self.size -= 1
            return True
        while temp.next != None:
            if temp.next.value == delValue:
                temp.next = temp.next.next
                self.size -= 1
                return True
            temp = temp.next
        return False

    def isPresent(self, data):
        #Serch a value in linked list
        temp = self.head
        while temp != None:
            if temp.value == data:
                return True
            temp = temp.next
        return False

class Solution():
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
        

ll = LinkedList()
s = Solution()
ll.addHead(8)
ll.addTail(7)
ll.addTail(6)
ll.addTail(5)
ll.addTail(85)
ll.addTail(54)
ll.addTail(65)
ll.addTail(32)
ll.addTail(12)
ll.addTail(78)
ll.addTail(25)
ll.addTail(0)
ll.addTail(-1)
ll.printList()
print("=========")
s.printList(ll.head)