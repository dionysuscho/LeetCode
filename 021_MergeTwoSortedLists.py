# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    """

    if l1 is None and l2 is not None:
        return l2
    if l1 is not None and l2 is None:
        return l1
    if l1 is None and l2 is None:
        return None

    curr1 = l1
    curr2 = l2
    curr0_start = curr0 = ListNode(0)

    while curr1 is not None and curr2 is not None:
        if curr1.val <= curr2.val:
            curr0.next = curr1
            curr1 = curr1.next
        else:
            curr0.next = curr2
            curr2 = curr2.next
        curr0 = curr0.next

    if curr1 is None:
        curr0.next = curr2
    elif curr2 is None:
        curr0.next = curr1

    return curr0_start.next


# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists2(l1, l2.next)
        return l2

def mergeTwoLists3(self, l1, l2):

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1

    if l2.val <= l1.val:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2
