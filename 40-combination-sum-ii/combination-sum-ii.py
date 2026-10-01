class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort to place duplicates adjacent to each other
        candidates.sort()
        results = []
        
        def backtrack(start: int, remaining_target: int, current_path: list[int]):
            if remaining_target == 0:
                results.append(list(current_path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate elements at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Prune branches if the element exceeds the remaining target
                if candidates[i] > remaining_target:
                    break
                
                # Choose the element
                current_path.append(candidates[i])
                
                # Move to the next element (index i + 1 ensures each is used once)
                backtrack(i + 1, remaining_target - candidates[i], current_path)
                
                # Backtrack (remove the element)
                current_path.pop()
                
        backtrack(0, target, [])
        return results
