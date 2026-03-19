def twoSum(self, nums: List[int], target: int) -> List[int]:
    Dict = {}
    for i in range(len(nums)):
        Dict[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in Dict.keys() and i != Dict[target - nums[i]]:
            return [i, Dict[target - nums[i]]]