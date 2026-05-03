class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        cur_node = self.head
        for i in range(index):
            if cur_node == None:
                return -1
            cur_node = cur_node.next_node
        if cur_node == None:
            return -1
        return cur_node.val

    def insertHead(self, val: int) -> None:
        # Cases: 
        #   1. Empty Linked List
        #   2. single ele LL
        #   3. LL
        new_node = ListNode(val)
        new_node.next_node = self.head
        if self.head == None:
            self.tail = new_node
        self.head = new_node
        return

    def insertTail(self, val: int) -> None:
        # Cases: 
        #   1. Empty Linked List
        #   2. single ele LL
        #   3. LL
        new_node = ListNode(val)
        if self.head == None: # For Empty Linked List
            self.head = new_node
            self.tail = new_node
            return

        # For Non Empty Linked List
        self.tail.next_node = new_node
        self.tail = new_node
        return

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        
        # Delete Only One Node in LL
        if self.head == self.tail:
            cur_node = self.head
            self.head = self.tail = None
            del cur_node
            return True if index == 0 else False
        
        # delete one node for multi node LL
        # head, tail and middle node deletion
        if index == 0:
            cur_node = self.head
            self.head = cur_node.next_node
            del cur_node
            return True
        cur_node = self.head
        parent_node = None
        for i in range(index):
            if cur_node == None:
                return False
            parent_node = cur_node
            cur_node = cur_node.next_node
        if parent_node == None:
            self.head = cur_node.next_node
        elif cur_node == self.tail:
            self.tail = parent_node
        else:
            parent_node.next_node = cur_node.next_node
        del cur_node
        return True

    def getValues(self) -> List[int]:
        list =[]
        cur_node = self.head
        while cur_node != None:
            list.append(cur_node.val)
            cur_node = cur_node.next_node
        return list
