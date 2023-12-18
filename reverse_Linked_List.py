# Fibonacci sequence like
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self. next = next
        
class Answer:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev


node1 = ListNode("5")
node1.next = ListNode("1")
node1.next.next = ListNode("3")
node1.next.next.next = ListNode("10")

ans = Answer()
head = ans.reverseLinkedList(node1)

arr1 = []
while head :
    arr1.append(head.val)
    head = head.next
print(arr1)
