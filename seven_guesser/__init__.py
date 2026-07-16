import check50

@check50.check()
def exists():
    """seven_guesser.py exists"""
    check50.exists("seven_guesser.py")

@check50.check(exists)
def test_turn1_win():
    """Guessing right on turn 1 wins and quits"""
    check50.run("python3 seven_guesser.py").stdin("7", prompt=True).stdout(".*[Ww]in.*", regex=True).exit()
