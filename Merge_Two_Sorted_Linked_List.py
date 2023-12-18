# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Answer:
    def mergeSortedList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
        
        
node1 = ListNode("1")
node1.next = ListNode("5")
node1.next.next = ListNode("7")

node2 = ListNode("3")
node2.next = ListNode("5")
node2.next.next = ListNode("9")

ans = Answer()
head = ans.mergeSortedList(node1, node2)

arr1 = []
while head :
    arr1.append(head.val)
    head = head.next
print(arr1)
