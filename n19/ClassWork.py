# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = ListNode(value)
#         self.length = 1

#     def append(self, value):
#         current_node = self.head

#         while current_node.next is not None:
#             current_node = current_node.next

#         new_node = ListNode(value)
#         current_node.next = new_node
#         self.length += 1

#     def insert(self, value, index):
#         last_index = self.length - 1
#         i = 0

#         if index == 0:
#             old_head = self.head
#             self.head = ListNode(value)
#             self.head.next = old_head
#             self.length += 1

#         elif index == last_index+1:
#             self.append(value)

#         elif 0 < index < last_index + 1:
#             current_node = self.head

#             while i != index-1:
#                 current_node = current_node.next
#                 i += 1

#             new_node = ListNode(value)
#             new_node.next = current_node.next
#             current_node.next = new_node
#             self.length += 1

#         elif index > last_index + 1 or index < 0:
#             print("Index Is Out Of Range")


#     def printList(self):
#         current_node = self.head
#         print(f"{current_node.value} ->", end="")

#         while current_node.next is not None:
#             current_node = current_node.next
#             print(f" {current_node.value} ->", end="")



# linked_list = LinkedList(0)


# linked_list.append(1)
# linked_list.append(5)
# linked_list.insert(2, 2)
# linked_list.insert(3, 3)
# linked_list.insert(4, 4)
# linked_list.insert(7, 0)
# linked_list.insert(10, 7)
# print(linked_list.length)
# linked_list.printList()

########################################

# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = ListNode(value)
#         self.length = 1

#     def append(self, value):
#         current_node = self.head

#         while current_node.next is not None:
#             current_node = current_node.next

#         new_node = ListNode(value)
#         current_node.next = new_node
#         self.length += 1

#     def insert(self, value, index):
#         last_index = self.length - 1
#         i = 0

#         if index == 0:
#             old_head = self.head
#             self.head = ListNode(value)
#             self.head.next = old_head
#             self.length += 1

#         elif index == last_index+1:
#             self.append(value)

#         elif 0 < index < last_index + 1:
#             current_node = self.head

#             while i != index-1:
#                 current_node = current_node.next
#                 i += 1

#             new_node = ListNode(value)
#             new_node.next = current_node.next
#             current_node.next = new_node
#             self.length += 1

#         elif index > last_index + 1 or index < 0:
#             print("Index Is Out Of Range")


#     def remove(self, index):
#         last_index = self.length - 1
#         i = 0

#         if index == 0:
#             self.head = self.head.next
#             self.length -= 1

#         elif index == last_index:
#             current_node = self.head

#             while i < last_index - 1:
#                 current_node = current_node.next
#                 i += 1

#             current_node.next = None
#             self.length -= 1

#         elif 0 < index < last_index:
#             current_node = self.head
#             while i != index - 1:
#                 current_node = current_node.next
#                 i += 1

#             deleted_element = current_node.next
#             current_node.next = deleted_element.next
#             self.length -= 1

#         elif index > last_index + 1 or index < 0:
#             print("Index Is Out Of Range")




#     def printList(self):
#         current_node = self.head
#         print(f"{current_node.value} ->", end="")

#         while current_node.next is not None:
#             current_node = current_node.next
#             print(f" {current_node.value} ->", end="")



# linked_list = LinkedList(0)


# linked_list.append(1)
# linked_list.append(5)
# linked_list.insert(2, 2)
# linked_list.insert(3, 3)
# linked_list.insert(4, 4)

# linked_list.remove(3)
# print(linked_list.length)
# linked_list.printList()


######################################

# class StackNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class Stack:
#     def __init__(self, value):
#         self.head = StackNode(value)
#         self.length = 1

#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next


#     def printList(self):
#         for node in self:
#             print(f"{node.value} -> ", end="")
#         print()


#     def size(self):
#         return self.length

#     def empty(self):
#         return self.length == 0

#     def top(self):
#         if self.empty():
#             raise Exception("The Stack is Empty")
#         return self.head.value

#     def push(self, value):
#         old_head = self.head
#         self.head = StackNode(value)
#         self.head.next = old_head
#         self.length += 1

#     def pop(self):
#         if self.empty():
#             raise Exception("The Stack is Empty")
#         # assert not self.empty(), "The Stack is Empty"
#         removed = self.head
#         self.head = self.head.next
#         self.length -= 1

#         return removed.value


# stack = Stack(10)
# stack.push(11)
# stack.push(21)
# stack.push(31)

# print(stack.pop())
# stack.printList()
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.top())

# # def my_generator(n):
# #     value = 0
# #
# #     while value < n:
# #         yield value
# #         value += 1
# #
# #
# # for value in my_generator(3):
# #     print(value)

#####################################
# class Register:
#     def __init__(self, username, password):
#         assert len(username) > 3, "Username is very Short!"
#         assert len(password) > 8, "Password is too Short"

#         self.username = username
#         self.__password = password

#     @property
#     def password(self):
#         return self.__password

#     @password.setter
#     def password(self, new_password):
#         old_password = input("Enter previous password: ")
#         if old_password == self.__password:
#             assert len(new_password) > 8, "Password is too Short"
#             self.__password = new_password

#     # @password.getter
#     # def password(self):
#     #     return f"Your current password is: {self.__password}"


# registration = Register("Nika", "HelloWorld2024")
# # print(registration.password)
# # registration.password = "HiNewPassword"
# # print(registration.password)
# # registration.password = "HiEveryone"
# print(registration.password)