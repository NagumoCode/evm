class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            my_map[sorted_word].append(word)

        return list(my_map.values())