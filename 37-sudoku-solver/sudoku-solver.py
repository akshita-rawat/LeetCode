class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Track presence of numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Initialize sets with the existing numbers on the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        def backtrack(cell_idx: int) -> bool:
            # If we filled all empty cells, a valid solution is found
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try numbers 1 to 9
            for digit in map(str, range(1, 10)):
                if (digit not in rows[r]) and (digit not in cols[c]) and (digit not in boxes[box_idx]):
                    # Place the digit (Choose)
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Recurse to fill the next cell (Explore)
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Remove the digit if it leads to a dead end (Un-choose)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
                    
            return False

        backtrack(0)
