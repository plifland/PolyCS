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
    """Runs a blinker 10 generations"""
    board = check50.run("python3 game_of_life.py boards/blinker.txt").stdin("10").stdout(timeout=20)
    check_board(board, "boards/blinker.txt")

@check50.check(exists)
def test_pulsar():
    """Runs a pulsar 12 generations"""
    board = check50.run("python3 game_of_life.py boards/pulsar.txt").stdin("12").stdout(timeout=20)
    check_board(board, "boards/pulsar.txt")

@check50.check(exists)
def test_spaceship():
    """Runs a heavy weight spaceship 10 generations"""
    board = check50.run("python3 game_of_life.py boards/heavyWeightSpaceship.txt").stdin("10").stdout(timeout=20)
    check_board(board, "boards/heavyWeightSpaceship_after10.txt")

@check50.check(exists)
def test_reject_nofile():
    """demands a file passed in"""
    check50.run("python3 game_of_life.py").exit()

@check50.check(exists)
def test_reject_negative():
    """rejects a negative generation count like -1"""
    check50.run("python3 game_of_life.py boards/blinker.txt").stdin("-1").reject()

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric generation count of "foo" """
    check50.run("python3 game_of_life.py boards/blinker.txt").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects an empty generation count of "" """
    check50.run("python3 game_of_life.py boards/blinker.txt").stdin("").reject()

def check_board(board, source):
    # Get only the final drawn board
    board = board.split("\x1b[H\x1b[2J")[-1]

    # Get the two characters likely used to draw
    char_cnts = Counter(board.replace("\n", ""))

    # Replace the user characters with 0,1 like the source file
    board = board.replace(char_cnts.most_common(2)[0][0], "0")
    board = board.replace(char_cnts.most_common(2)[1][0], "1")

    expected = open(source, encoding="utf-8-sig").read()
    help = "\n\tIf you changed the looks of your board dramatically, it might not match and that's ok!\n\nHere is your board:\n" + board + "\n\nAnd here is the solution:\n" + expected
    if not match(expected, board):
        if len(expected) == len(board) - 1:
          help = "\n\tWatch out - the text file has a strange whitespace character that you are turning into a cell!\n\tMake sure you encode only 0s and 1s\n"
        raise check50.Mismatch(expected, board, help=help)