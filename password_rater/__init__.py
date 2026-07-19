import check50

@check50.check()
def exists():
    """password_rater.py exists."""
    check50.exists("password_rater.py")

@check50.check(exists)
def test1():
    """identifies password as WEAK"""
    check50.run("python3 password_rater.py").stdin("password").stdout("WEAK\n").exit()

@check50.check(exists)
def test2():
    """identifies Password as WEAK"""
    check50.run("python3 password_rater.py").stdin("Password").stdout("WEAK\n").exit()

@check50.check(exists)
def test3():
    """everything but length is STRONG"""
    check50.run("python3 password_rater.py").stdin("P@$sW0rd").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(exists)
def test4():
    """everything but lower is STRONG"""
    check50.run("python3 password_rater.py").stdin("HOWISITPOSSIBLETONOTHAVELOWER?42").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(exists)
def test5():
    """everything but upper is STRONG"""
    check50.run("python3 password_rater.py").stdin("thishaseverything!exceptuppercharacters2024").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(exists)
def test6():
    """everything but number is STRONG"""
    check50.run("python3 password_rater.py").stdin("thisHasEverything!exceptNumbers:(").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(exists)
def test7():
    """everything but special is MEDIUM"""
    check50.run("python3 password_rater.py").stdin("theNoSpecialSpecialOfY2K").stdout("MEDIUM\n").exit()

@check50.check(exists)
def test8():
    """everything but middle special is STRONG"""
    check50.run("python3 password_rater.py").stdin("CorrectHorseBatterySt4ple!").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(exists)
def test9():
    """everything is VERY STRONG"""
    check50.run("python3 password_rater.py").stdin("Bkx4UHM@$#g5zZ4etd2V").stdout("VERY STRONG\n").exit()
