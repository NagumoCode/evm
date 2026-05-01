class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Найти середину
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Развернуть вторую половину
        second = slow.next
        slow.next = None  # Отрезаем первую половину
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. Слить две половины
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2