from collections import deque
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n

        flat = deque([x for row in grid for x in row])

        for i in range(k):
            flat.appendleft(flat.pop())

        res = [list(flat)[i*n:(i+1)*n] for i in range(m)]

        return res 

#Time Complexity: O(m*n)
#Space Complexity: O(m*n)
'''
Approach:
1.  First, we find the number of rows (m) and columns (n) in the grid.
2.  We then calculate the effective number of shifts needed by taking k modulo (m*n),
    since shifting the grid m*n times results in the same grid.
3.  We flatten the 2D grid into a 1D deque called 'flat'
4.  We then perform k shifts by popping the last element of the deque and appending it to the front of the deque.
5.  Finally, we return the reshaped list 'res' as a 2D grid by slicing the deque into rows of length n.

why deque is used:
A deque (double-ended queue) is used here because it allows for efficient popping from the end and appending to the front, 
which is exactly what we need for the shifting operation. 
This makes the shifting operation O(k) instead of O(k*n) if we were to use a list, 
as lists would require O(n) time to shift elements.

why better than the previous solution:
1.  The previous solution creates a new list for the shifted elements, which takes O(m*n) time and space.
2.  The deque solution performs the shifts in O(k) time and uses O(m*n) space for the flattened grid, 
    making it more efficient for larger values of k.  
'''