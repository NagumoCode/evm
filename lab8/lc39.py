class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, current_comb, total):
            if total == target:
                res.append(current_comb.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current_comb.append(candidates[i])
            dfs(i, current_comb, total + candidates[i])

            current_comb.pop()
            dfs(i + 1, current_comb, total)

        dfs(0, [], 0)
        return res