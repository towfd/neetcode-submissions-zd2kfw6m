from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Optimal One-Pass Solution
        # We use hash sets to keep track of the digits we've seen in each row, column, and 3x3 box.
        # This allows us to validate the board by iterating through it only exactly once.
        
        # Time Complexity: O(1) strictly since the board is always 9x9. 
        # (Or O(N^2) if generalized to an N x N board).
        # Space Complexity: O(1) strictly, as the maximum number of elements in all sets combined is 81.
        
        # Initialize dictionaries where each key maps to a Set.
        # This prevents KeyError when we try to add or check items for the first time.
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # Key will be a tuple: (row // 3, col // 3)
        
        for r in range(9):
            for c in range(9):
                current_val = board[r][c]
                
                # Skip empty cells
                if current_val == ".":
                    continue
                    
                # Check if the current value already exists in the corresponding row, col, or box
                if (current_val in rows[r] or 
                    current_val in cols[c] or 
                    current_val in boxes[(r // 3, c // 3)]):
                    return False # Found a duplicate, invalid Sudoku!
                
                # If not found, add the value to our tracker sets
                rows[r].add(current_val)
                cols[c].add(current_val)
                boxes[(r // 3, c // 3)].add(current_val)
                
        # If we successfully iterate through the entire board without conflicts, it's valid!
        return True