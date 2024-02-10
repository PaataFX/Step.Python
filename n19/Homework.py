class ListNode:
    def __init__(self, value):
        self.value = value  # Initializes a node with a value
        self.next = None    # Points to the next node in the linked list (initialized as None)


class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)  # Initializes the linked list with a head node containing a value
        self.length = 1              # Tracks the length of the linked list (initialized as 1)

    def append(self, value):
        current_node = self.head  # Starts at the head node

        while current_node.next is not None:  # Traverses to the end of the linked list
            current_node = current_node.next

        new_node = ListNode(value)  # Creates a new node with the given value
        current_node.next = new_node  # Adds the new node at the end of the linked list
        self.length += 1              # Increments the length of the linked list

    def insert(self, value, index):
        last_index = self.length - 1  # Calculates the index of the last element
        i = 0

        if index == 0:  # Inserts at the beginning of the linked list
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            self.length += 1

        elif index == last_index+1:  # Inserts at the end of the linked list
            self.append(value)

        elif 0 < index < last_index + 1:  # Inserts at a specific index within the linked list
            current_node = self.head

            while i != index-1:
                current_node = current_node.next
                i += 1

            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

        elif index > last_index + 1 or index < 0:  # Handles out of range index
            print("Index Is Out Of Range")

    def remove(self, index):
        last_index = self.length - 1
        i = 0

        if index == 0:  # Removes the first node in the linked list
            self.head = self.head.next
            self.length -= 1

        elif index == last_index:  # Removes the last node in the linked list
            current_node = self.head

            while i < last_index - 1:
                current_node = current_node.next
                i += 1

            current_node.next = None
            self.length -= 1

        elif 0 < index < last_index:  # Removes a node from a specific index
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            deleted_element = current_node.next
            current_node.next = deleted_element.next
            self.length -= 1

        elif index > last_index + 1 or index < 0:  # Handles out of range index
            print("Index Is Out Of Range")

    def printList(self):
        current_node = self.head
        print(f"{current_node.value} ->", end="")  # Prints the value of the current node

        while current_node.next is not None:  # Traverses and prints the values of the linked list
            current_node = current_node.next
            print(f" {current_node.value} ->", end="")

linked_list = LinkedList(0)  # Creates a linked list with an initial value of 0

linked_list.append(1)  # Appends 1 to the linked list
linked_list.append(5)  # Appends 5 to the linked list
linked_list.insert(2, 2)  # Inserts 2 at index 2
linked_list.insert(3, 3)  # Inserts 3 at index 3
linked_list.insert(4, 4)  # Inserts 4 at index 4

linked_list.remove(3)  # Removes element at index 3
print(linked_list.length)  # Prints the length of the linked list
linked_list.printList()  # Prints the linked list
