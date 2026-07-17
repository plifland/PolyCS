import check50

from collections import Counter
from re import match

@check50.check()
def exists():
    """automata_board.py exists."""
    check50.exists("automata_board.py")
    check50.include("boards")

@check50.check(exists)
def test_blinker():
    """Prints the tiny 3x3 blinker.txt board"""
    board = check50.run("python3 automata_board.py boards/blinker.txt").stdout()
    check_board(board, "boards/blinker.txt")

def check_board(board, source):
    # Get the two characters likely used to draw
    char_cnts = Counter(board)

    # Replace the user characters with 0,1 like the source file
    board = board.replace(char_cnts.most_common(2)[0][0], "0")
    board = board.replace(char_cnts.most_common(2)[1][0], "1")

    expected = open(source, encoding="utf-8-sig").read()

    help = ""
    if not match(expected, board):
        raise check50.Mismatch(expected, board, help=help)