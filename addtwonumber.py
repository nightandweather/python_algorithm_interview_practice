class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        n = str(self.toInt(l1) + self.toInt(l2))
        for idx, char in enumerate(n):
            if idx == 0:
                y = ListNode(val=char, next=None)
            else:
                y = ListNode(val=char, next=y)
        return y                        
    
    def toInt(self, l: ListNode) -> int:
        s = ''        
        while l:
            s += str(l.val)
            l = l.next
        return int(s[::-1])