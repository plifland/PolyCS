import check50

@check50.check()
def exists():
    """seven_guesser.py exists"""
    check50.exists("seven_guesser.py")

@check50.check(exists)
def test_turn1_win():
    """Guessing right on the first guess wins and quits"""
    check50.run("python3 seven_guesser.py").stdin("7", prompt=True).stdout(".*[Ww]in.*", regex=True).exit()

@check50.check(exists)
def test_turn2_win():
    """Guessing right on the second guess wins and quits"""
    check50.run("python3 seven_guesser.py").stdin("2", prompt=True).stdin("7", prompt=True).stdout(".*[Ww]in.*", regex=True).exit()

@check50.check(exists)
def test_turn3_win():
    """Guessing right on the third guess wins and quits"""
    check50.run("python3 seven_guesser.py").stdin("2", prompt=True).stdin("2", prompt=True).stdin("7", prompt=True).stdout(".*[Ww]in.*", regex=True).exit()

@check50.check(exists)
def test_too_low():
    """Guessing too low on the first guesss says 'Too low'"""
    check50.run("python3 seven_guesser.py").stdin("3", prompt=True).stdout(".*[Tt]oo low.*", regex=True).stdin("7", prompt=True).exit()

@check50.check(exists)
def test_too_high():
    """Guessing too high on the first guesss says 'Too high'"""
    check50.run("python3 seven_guesser.py").stdin("8", prompt=True).stdout(".*[Tt]oo high.*", regex=True).stdin("7", prompt=True).exit()

@check50.check(exists)
def test_too_low2():
    """Guessing too low on the second guesss says 'Too low'"""
    check50.run("python3 seven_guesser.py").stdin("8", prompt=True).stdin("3", prompt=True).stdout(".*[Tt]oo low.*", regex=True).stdin("7", prompt=True).exit()

@check50.check(exists)
def test_too_high2():
    """Guessing too high on the second guesss says 'Too high'"""
    check50.run("python3 seven_guesser.py").stdin("3", prompt=True).stdin("8", prompt=True).stdout(".*[Tt]oo high.*", regex=True).stdin("7", prompt=True).exit()

@check50.check(exists)
def test_lose():
    """Guessing wrong three times loses"""
    check50.run("python3 seven_guesser.py").stdin("3", prompt=True).stdin("8", prompt=True).stdin("5", prompt=True).stdout(".*[Ll]ose.*", regex=True).exit()
