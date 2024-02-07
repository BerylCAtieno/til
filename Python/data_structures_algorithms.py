"""Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false."""

def exist(board, word):
    def dfs(board, word, i, j, k):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        temp, board[i][j] = board[i][j], '/'
        res = dfs(board, word, i + 1, j, k + 1) or dfs(board, word, i - 1, j, k + 1) \
            or dfs(board, word, i, j + 1, k + 1) or dfs(board, word, i, j - 1, k + 1)
        board[i][j] = temp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True
    return False

# Example usage:
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(exist(board, "ABCCED"))  # Output: True
print(exist(board, "SEE"))     # Output: True
print(exist(board, "ABCB"))    # Output: False


#Explanation

"""We define a nested function dfs that performs depth-first search starting from a given position (i, j) in the grid.
Within dfs, we check if the current cell matches the corresponding character in the word. If not, or if we reach the end of the word, we return False.
Otherwise, we mark the current cell as visited (by changing its value to '/'), and recursively explore its neighboring cells in all four directions.
If any of the recursive calls return True, indicating that the word can be formed starting from the current cell, we return True.
If none of the recursive calls succeed, we restore the original value of the current cell and return False.
We then iterate through all cells in the grid and call dfs starting from each cell. If any call returns True, we return True. If no call returns True, we return False at the end."""

#Algorithm and Complexity

"""
The algorithm provided is a Depth-First Search (DFS) algorithm, which is a type of graph traversal algorithm commonly used for exploring nodes and edges in a graph or in this case, a 2D grid.

Type of Algorithm: Depth-First Search (DFS)"""