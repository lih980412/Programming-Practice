class Stack:
    def __init__(self):
        self.queue = []

    def add_val(self, val):
        self.queue.append(val)

    def pop_val(self):
        value = self.queue.pop()
        return value



if __name__ == "__main__":
    stack = Stack()

    stack.add_val(3)
    stack.add_val(5)
    stack.add_val(7)

    a = stack.pop_val()
    print(a)


# s = "()"
# stack = Stack()
# for i in s:
#     if i in ['(', '{', '[']:
#         stack.add_val(i)
#
#
#
#     elif i == ')':
#         if stack.pop_val() == '(':
#             continue
#         else:
#             print("False")
#     elif i == '}':
#         if stack.pop_val == '{':
#             continue
#         else:
#             print("False")
#     elif i == ']':
#         if stack.pop_val == '[':
#             continue
#         else:
#             print("False")
#
# print("True")
