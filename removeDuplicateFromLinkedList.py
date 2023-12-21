# Remove Duplicates value in LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self. next = next
        
class Answer:
    def removeDuplicateFromLinkedList(self, head: ListNode) -> ListNode:
        
        curr = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next                  # move the curr pointer next until duplicate 
            curr = curr.next
            
        return head

node1 = ListNode("5")
node1.next = ListNode("5")
node1.next.next = ListNode("1")
node1.next.next.next = ListNode("10")
node1.next.next.next.next = ListNode("10")
node1.next.next.next.next = ListNode("12")

ans = Answer()
head = ans.removeDuplicateFromLinkedList(node1)

arr1 = []
while head :
    arr1.append(head.val)
    head = head.next
print(arr1)
