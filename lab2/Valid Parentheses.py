class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {']': '[', ')': '(', '}':'{'}
        my_stack = []
        for i in s:
            if i in hash_table.values():
                my_stack.append(i)
            else:
                if len(my_stack) != 0 and my_stack[-1] == hash_table[i]:
                    my_stack.pop()
                else:
                    return False
        if len(my_stack) == 0:
            return True
        return False