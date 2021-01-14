# SudokuSolver
Attempting to follow along a Sudoku Solver tutorial done by TechWithTim in hopes of improving understanding and implementing more algorithms. A Sudoku is a puzzle that consists of 9 blocks, with each block containing 8 units, having a total of 81 units. Each unit will be labeled #1-9. The game will randomly provide a partially filled grid and the goal is to fill out each empty unit with a value that is not within the same row/column/diagonal of the entire matrix. The user will be able to attempt to solve and be able to select to give up and let it solve itself.

 # How to approach the solution?
 We would have to develop all possible solutions for each position/unit we are in, that way if there are no solutions we are able to break out of the loop.
 
 # What is "backtracking"?
 Backtracking is when you get to a position where the solution/option is not valid (meaning that there is no action left to be taken) that you will return to the previous position (backtrack) that is in a valid state. 
 
 # How to approach backtracking for the Sudoku Solver?
 We would have to check every possible value in that unit if it's "valid" by iterating through the range,length, and position of the matrix (board) using checkValid(). If not valid then the code needs to reset the unit we just filled, and backtrack to the next valid solution.

