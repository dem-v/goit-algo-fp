class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Сортування вставками
    def sort(self):
        cur = self.head
        while cur:
            next = cur.next
            while next:
                if cur.data > next.data:
                    cur.data, next.data = next.data, cur.data
                next = next.next
            cur = cur.next


def merge_two_sorted_llists(left_list: LinkedList, right_list: LinkedList):
    if left_list is None:
        return right_list
    if right_list is None:
        return left_list
    res_list = LinkedList()
    curr_left = left_list.head
    curr_right = right_list.head
    while curr_left and curr_right:
        if curr_left.data < curr_right.data:
            res_list.insert_at_end(curr_left.data)
            curr_left = curr_left.next
        else:
            res_list.insert_at_end(curr_right.data)
            curr_right = curr_right.next
    while curr_left:
        res_list.insert_at_end(curr_left.data)
        curr_left = curr_left.next
    while curr_right:
        res_list.insert_at_end(curr_right.data)
        curr_right = curr_right.next
    return res_list


if __name__ == '__main__':
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(20)

    # Вставляємо вузли в кінець
    llist.insert_at_end(15)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    print('\nРозвернутий список: ')
    llist.reverse()
    llist.print_list()

    print('\nВідсортований список: ')
    llist.sort()
    llist.print_list()

    print('\nОбєднання двох списків: ')
    llist2 = LinkedList()
    llist2.insert_at_beginning(1)
    llist2.insert_at_beginning(16)
    llist2.insert_at_beginning(19)
    llist2.insert_at_end(25)
    llist2.sort()

    llist3 = merge_two_sorted_llists(llist, llist2)
    llist3.print_list()
