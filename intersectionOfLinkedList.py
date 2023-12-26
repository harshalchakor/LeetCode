# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Answer:
    def intersectionOfLinkedList(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        l1, l2 = headA, headB
        
        while l1 != l2:
            
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
            
        return l1
        
node1 = ListNode("1")
node1.next = ListNode("5")
node1.next.next = ListNode("7")
node1.next.next.next = ListNode("9")
node1.next.next.next.next = ListNode("10")

node2 = ListNode("3")
node2.next = ListNode("5")
node2.next.next = node1.next.next.next
node2.next.next.next = node1.next.next.next.next

#Function call
ans = Answer()
head = ans.intersectionOfLinkedList(node1, node2)

#output
arr1 = []
while head :
    arr1.append(head.val)
    head = head.next
print(arr1)
