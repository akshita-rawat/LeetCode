class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(remain, combo, start):
            if remain == 0:
                # Found a valid combination
                res.append(list(combo))
                return
            elif remain < 0:
                # Exceeded the target sum
                return
            
            for i in range(start, len(candidates)):
                # Include the current candidate
                combo.append(candidates[i])
                # Provide the same index i to allow re-using the same element
                backtrack(remain - candidates[i], combo, i)
                # Backtrack to try another candidate
                combo.pop()
                
        backtrack(target, [], 0)
        return res
