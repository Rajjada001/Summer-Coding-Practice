class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self, data):
        head = self.head
        node = Node(data, head)
        head = node

    def append(self, x):
        if self.head is None:
            head = x
        


    def printLL(self):
        if self.head == None:
            print("List is empty")
        else:
            temp= self.head
            while temp != None:
                print(temp.next, end=" ")
                temp = temp.next
            print()

ll1 = LinkedList()
ll1.append(1)
ll1.printLL()
