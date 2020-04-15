"""
https://app.codesignal.com/tournaments/qhfBzmNJ5uGu7rxha/B

> Task
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically
and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image
below to see all valid moves for a knight piece that is placed on one of the central squares.

> Example
For cell = "a1", the output should be 2.
For cell = "c2", the output should be 6.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string cell
String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.
- guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.
- output: integer
"""


def chess_knight_moves(cell):
    def is_valid(pos):
        if 0 <= pos < 8:
            return True
        return False

    def get_x(pos):
        return ord(pos) - ord('a')

    def get_y(pos):
        return ord(pos) - ord('1')

    current_x = get_x(cell[0])
    current_y = get_y(cell[1])
    result = 0

    print("x: {}".format(current_x))
    print("y: {}".format(current_y))

    # make a range all around the knight.
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            print("{}; {}".format(dx, dy))
            result += 2
    return result
