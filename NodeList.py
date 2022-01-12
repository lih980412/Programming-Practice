class Node:
    def __init__(self, value):
        self.value = value
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def addatEnd(self, num):
        node_new = Node(num)
        index = self.headval
        while index.nextval:
            index = index.nextval
        index.nextval = node_new

    def addatBegin(self, num):
        node_new = Node(num)
        node_new.nextval = self.headval
        self.headval = node_new

    def listPrint(self):
        index = self.headval
        while index.nextval:
            print(index.value)
            index = index.nextval
        print(index.value)

    def addatNum1(self, tar_num, num):
        index = self.headval
        while index.nextval:
            if index.value == tar_num:
                break
            index = index.nextval
        if index.nextval or (not index.nextval and index.value == tar_num):
            new_node = Node(num)
            new_node.nextval = index.nextval
            index.nextval = new_node

    def addatNum(self, pre_node, num):
        index = self.headval
        while index.nextval:
            if index.value == pre_node.value:
                break
            index = index.nextval
        if index.nextval or (not index.nextval and index.value == pre_node.value):
            new_node = Node(num)
            new_node.nextval = index.nextval
            index.nextval = new_node

    def delNum(self, num):
        index = self.headval.nextval
        pre = self.headval
        if pre.value == num:
            self.headval = index
        while index.nextval:
            if index.value == num:
                break
            pre = index
            index = index.nextval
        if index.value == num:
            pre.nextval = index.nextval


# if __name__ == "__main__":
#     list1 = SLinkedList()
#     list1.headval = Node(3)
#     node2 = Node(4)
#     node4 = Node(6)
#     list1.headval.nextval = node4
#     node4.nextval = node2
#
#     index = list1.headval
#     list1.listPrint()
#     print("------------")
#
#     list1.addatEnd(8)
#     index = list1.headval
#     list1.listPrint()
#     print("------------")
#
#     list1.addatBegin(1)
#     list1.listPrint()
#     print("------------")
#
#     list1.addatNum1(1, 10)
#     list1.listPrint()
#     print("------------")
#
#     list1.delNum(66)
#     list1.listPrint()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addatEnd(self, num, a):
        node_new = ListNode(num)
        index = a
        while index.next:
            index = index.next
        index.next = node_new


# def mergeTwoLists(list1, list2):
#     if list1 is None:
#         return list2
#     elif list2 is None:
#         return list1
#
#     index1 = list1
#     index2 = list2
#
#     if index1.val > index2.val:
#         pre = index2
#         while index1:  # list1 和 list2 都不空
#             while index1.val > index2.val:  # 合并到 list2
#
#                 if index2.next:  # 如果 index2.next 非空，则移动指针
#
#                     index2 = index2.next
#                 else:  # 遍历到 list2 的末尾，则直接把 list1 连接至 list2 之后
#                     index2.next = index1
#                     return list2
#
#             if index1:
#                 temp = index1
#                 pre.next = temp
#                 temp.next = index2
#                 index1 = index1.next
#             else:
#                 return list2
#
#     else:
#         while index2:  # list1 和 list2 都不空
#             pre = index1
#             while index2.val < index1.val:  # 合并到 list1
#
#                 if index1.next:  # 如果 index1.next 非空，则移动指针
#
#                     index1 = index1.next
#                 else:  # 遍历到 list1 的末尾，则直接把 list2 连接至 list1 之后
#                     index1.next = index2
#                     return list1
#
#             if index2:
#                 temp = index2
#                 pre.next = temp
#                 temp.next = index1
#                 index2 = index2.next
#             else:
#                 return list1

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    if list1.val >= list2.val:  # l1 插入到 l2 中
        target = list2
        source = list1
        head = list2
    else:  # l2 插入到 l1 中
        target = list1
        source = list2
        head = list1

    while target:  # source 比 target 大
        if source:
            if source.val >= target.val:
                pre = target
                target = target.next
                continue
            else:
                temp = source
                pre.next = temp
                temp.next = target  # 插入

                pre = temp
                source = source.next
        else:
            break

    return head


a = ListNode(1)
a.addatEnd(ListNode(2), a)
a.addatEnd(ListNode(4), a)
b = ListNode(1)
b.addatEnd(ListNode(3), b)
b.addatEnd(ListNode(4), b)

print(1111)
print(mergeTwoLists(a, b))
