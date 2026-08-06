import check50

@check50.check()
def exists():
    """SevenGuesser exists"""
    check50.exists("SevenGuesser.java")

@check50.check(exists)
def compiles():
    """SevenGuesser.java compiles"""
    check50.run("javac SevenGuesser.java").exit(0)

@check50.check(compiles)
def test_turn1_win():
    """Guessing right on the first guess wins and quits"""
    check50.run("java SevenGuesser").stdin("7").stdout(".*[Ww]in.*").exit()

@check50.check(compiles)
def test_turn2_win():
    """Guessing right on the second guess wins and quits"""
    check50.run("java SevenGuesser").stdin("2").stdin("7").stdout(".*[Ww]in.*").exit()

@check50.check(compiles)
def test_turn3_win():
    """Guessing right on the third guess wins and quits"""
    check50.run("java SevenGuesser").stdin("2").stdin("2").stdin("7").stdout(".*[Ww]in.*").exit()

@check50.check(compiles)
def test_too_low():
    """Guessing too low on the first guess says 'Too low'"""
    check50.run("java SevenGuesser").stdin("3").stdout(".*[Tt]oo low.*").kill()

@check50.check(compiles)
def test_too_high():
    """Guessing too high on the first guess says 'Too high'"""
    check50.run("java SevenGuesser").stdin("8").stdout(".*[Tt]oo high.*").kill()

@check50.check(compiles)
def test_too_low2():
    """Guessing too low on the second guess says 'Too low'"""
    check50.run("java SevenGuesser").stdin("8").stdin("3").stdout(".*[Tt]oo low.*").kill()

@check50.check(compiles)
def test_too_high2():
    """Guessing too high on the second guess says 'Too high'"""
    check50.run("java SevenGuesser").stdin("3").stdin("8").stdout(".*[Tt]oo high.*").kill()

@check50.check(compiles)
def test_lose():
    """Guessing wrong three times loses"""
    check50.run("java SevenGuesser").stdin("3").stdin("8").stdin("5").stdout(".*[Ll]os[et].*").exit()
