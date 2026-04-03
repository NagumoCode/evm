def lengthOfLongestSubstring(self, s: str) -> int:
    current_chars = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in current_chars:
            current_chars.remove(s[left])
            left += 1
        current_chars.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len