# Complete the printLinkedList function below.

# See the problem
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def printLinkedList(head):
    print(head.data)
    while head.next != None:
        head = head.next
        print(head.data)
        

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)