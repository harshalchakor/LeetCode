# Fibonacci sequence like
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self. next = next
        
class Answer:
    def removeFromLinkedList(self, head: ListNode, value) -> ListNode:
        
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        
        while curr:
            
            if curr.val == value:
                prev.next = curr.next
            else:
                prev = curr
                
            curr = curr.next
            
        return dummy.next

node1 = ListNode("5")
node1.next = ListNode("1")
node1.next.next = ListNode("3")
node1.next.next.next = ListNode("10")

ans = Answer()
head = ans.removeFromLinkedList(node1, "1")

arr1 = []
while head :
    arr1.append(head.val)
    head = head.next
print(arr1)
