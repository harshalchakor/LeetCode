# Fibonacci sequence like
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self. next = next
        
class Answer:
    def PalindromLinkedList(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        
        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half of LinkedList
        prev = None
        
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
        # check if palindrom
        
        left, right = head, slow
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

node1 = ListNode("5")
node1.next = ListNode("1")
node1.next.next = ListNode("1")
node1.next.next.next = ListNode("5")

ans = Answer()
print(ans.PalindromLinkedList(node1))
