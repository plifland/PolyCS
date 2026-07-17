import check50

from collections import Counter
from re import match

@check50.check()
def exists():
    """game_of_life.py exists."""
    check50.exists("game_of_life.py")
    check50.include("boards")

@check50.check(exists)
def test_blinker():
    """Prints the tiny 3x3 Blinker board"""
    board = check50.run("python3 game_of_life.py boards/blinker.txt").stdin("10").stdout(timeout=20)
    check_board(board, "boards/blinker.txt")

@check50.check(exists)
def test_pulsar():
    """Prints the 17x17 Pulsar board"""
    board = check50.run("python3 game_of_life.py boards/pulsar.txt").stdin("10").stdout(timeout=20)
    check_board(board, "boards/pulsar.txt")

@check50.check(exists)
def test_spaceship():
    """Prints the rectangular Heavy Weight Spaceship board"""
    board = check50.run("python3 game_of_life.py boards/heavyWeightSpaceship.txt").stdin("10").stdout(timeout=20)
    check_board(board, "boards/heavyWeightSpaceship.txt")

def check_board(board, source):
    # Get only the final drawn board
    board = board.split("\x1b[H\x1b[2J")[-1]

    # Get the two characters likely used to draw
    char_cnts = Counter(board.replace("\n", ""))

    # Replace the user characters with 0,1 like the source file
    board = board.replace(char_cnts.most_common(2)[0][0], "0")
    board = board.replace(char_cnts.most_common(2)[1][0], "1")

    expected = open(source, encoding="utf-8-sig").read()
    help = board
    if not match(expected, board):
        if len(expected) == len(board) - 1:
          help = "\n\tWatch out - the text file has a strange whitespace character that you are turning into a cell!\n\tMake sure you encode only 0s and 1s\n"
        raise check50.Mismatch(expected, board, help=help)