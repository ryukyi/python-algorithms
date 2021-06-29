class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

#TODO:: InsertAfter 
class CircularLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None 

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.getNext()


    def printCLList(self):
        node = self.head
        while(node):
            print(node.value)
            if node.next == self.head:
                break
            node = node.getNext()


    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, value):
        node = Node(value)
        temp = self.head
         
        node.next = self.head
 
        # If linked list is not None (Meaning linkedList already contains at least one value)
        # If so move through the existing linked list till you find a node that has it's next value 
        # pointing back to the head (this is the last node)
        # When we do, set it to point to the new head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            #setting last node to point back to the new head
            temp.next = node
        # If it is an empty linked-list, set the new node to point to itself    
        else:
            node.next = node # For the first node
 
        # finally set the head of the linked-list to the new node
        self.head = node
            
    def append(self, value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            node.next = node
        else:
            current = self.head
            while current:
                if(current.next == self.head):
                    break
                else:
                    current = current.getNext()
            current.next = node
            node.next = self.head

    # Insert After using a value runs O(n), by using a node, it could run O(1)
    def insertAfter(self, valueToBeInsertedAFter, valueToBeInserted):
        pos = self.search(valueToBeInsertedAFter)
        if(pos == None):
           print("Value to be Inserted AFter does not exist")
        else:
            newNode = Node(valueToBeInserted)
            newNode.next = pos.next
            pos.next = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            if current.next == self.head:
                count += 1
                break;
            else:
                count += 1
                current = current.getNext()
        
        return count

    def search(self, value):
        current = self.head
        if current == None:
            return None

        while current:
            if(current.value == value):
                return current
            elif current.next == self.head:
                break
            else:
                current = current.next

        return None

    def delete(self, value):
        current = self.head
        prevNode = self.head
        found = False

        if current == None:
            print("LinkedList is already empty")

        while current:
            if current.value == value:
                found = True
                break
            elif current.next == self.head:
                break
            else:
                prevNode = current
                current = current.next

        if(found):
            if current == self.head:
                self.head = None
            else: 
                prevNode.next = current.next
        else:
            print("Couldn't find the value: ", value)

    def deleteLinkedList(self):
        if self.head == None:
            print("LinkedList is already empty")
        else:
            self.head = None


linkedList = CircularLinkedList()

# Push values to the begining of a linkedlist
linkedList.push(3)
linkedList.push(2)
linkedList.push(1)

# Append values to the emd of a linkedlist
linkedList.append(4)

# Insert value after another value --> insert 19 after 3
linkedList.insertAfter(2, 19)


# Iterate and print the values in the linkedList
linkedList.printCLList()

# Print linkedList as an array
print([node.value for node in linkedList])

print("VALUE:: ", linkedList.search(1).value)
print("VALUE:: ", linkedList.search(2).value)
print("VALUE:: ", linkedList.search(3).value)
print("VALUE:: ", linkedList.search(4).value)
print("VALUE:: ", linkedList.search(5))


# Delete nodes from linkedlist
linkedList.delete(2)
linkedList.delete(3)


print([node.value for node in linkedList])

# Delete entire linkedlist
linkedList.deleteLinkedList()
print([node.value for node in linkedList])