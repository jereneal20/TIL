class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def reverse(head):
    dummy = Node(-1)
    dummy.next = head
    node = dummy
    # 1 -> 4 -> 2 -> 3 -> 5

    last_odd = None
    while node:
        if node.data % 2 != 0:
            last_odd = node
            node = node.next
            continue

        while node.next and node.next.data % 2 == 0:
            node_to_move = node.next

            node.next = node_to_move.next
            node_to_move.next = last_odd.next
            last_odd.next = node_to_move

        node = node.next

    return dummy.next


  # head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  # expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  # output_1 = reverse(head_1)
  # check(expected_1, output_1)
  #
  # head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  # expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  # output_2 = reverse(head_2)
  # check(expected_2, output_2)