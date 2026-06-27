class list_node(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
class MyLinkedList(object):

    def __init__(self):
        self.dummy=list_node(0)
        self.size=0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        curr=self.dummy.next
        for _ in range(index):
            curr=curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size: return  
        if index < 0: index=0
        prev=self.dummy
        for _ in range(index):
            prev=prev.next
        new_node=list_node(val)
        new_node.next=prev.next
        prev.next=new_node
        self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:return
        prev=self.dummy
        for _ in range(index):
            prev=prev.next
        prev.next=prev.next.next
        self.size-=1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)