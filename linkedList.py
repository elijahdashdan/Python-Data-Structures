class Node:
    def __init__ (self, data=None, next=None):
        self.data = data
        self.next = next

class DoubleNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data= data
        self.next= next
        self.prev= prev


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)
    
    def insertAtEnd(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr= itr.next
        
        itr.next = Node(data, None)
    
    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insertAtEnd(data)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Not valid index")
            
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insertAt(self, index,data):
        if index < 0 or index >= self.getLength():
            raise Exception("Not valid index")

        if index == 0:
            self.insertAtBeginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        if data_after == None:
            raise Exception("No Data")
         
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next= node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            
            if itr.next.data == data:
                itr.next = itr.next.next
            itr = itr.next
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("apple") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
