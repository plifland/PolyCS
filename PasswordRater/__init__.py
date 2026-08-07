import check50

@check50.check()
def exists():
    """PasswordRater.java exists."""
    check50.exists("PasswordRater.java")

@check50.check(exists)
def compiles():
    """PasswordRater.java compiles"""
    check50.run("javac PasswordRater.java").exit(0)

@check50.check(compiles)
def test1():
    """identifies password as WEAK"""
    check50.run("java PasswordRater").stdin("password").stdout("WEAK\n").exit()

@check50.check(compiles)
def test2():
    """identifies Password as WEAK"""
    check50.run("java PasswordRater").stdin("Password").stdout("WEAK\n").exit()

@check50.check(compiles)
def test3():
    """everything but length is STRONG"""
    check50.run("java PasswordRater").stdin("P@$sW0rd").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(compiles)
def test4():
    """everything but lower is STRONG"""
    check50.run("java PasswordRater").stdin("HOWISITPOSSIBLETONOTHAVELOWER?42").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(compiles)
def test5():
    """everything but upper is STRONG"""
    check50.run("java PasswordRater").stdin("thishaseverything!exceptuppercharacters2024").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(compiles)
def test6():
    """everything but number is STRONG"""
    check50.run("java PasswordRater").stdin("thisHasEverything!exceptNumbers:(").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(compiles)
def test7():
    """everything but special is MEDIUM"""
    check50.run("java PasswordRater").stdin("theNoSpecialSpecialOfY2K").stdout("MEDIUM\n").exit()

@check50.check(compiles)
def test8():
    """everything but middle special is STRONG"""
    check50.run("java PasswordRater").stdin("CorrectHorseBatterySt4ple!").stdout("^STRONG\n", "STRONG\n").exit()

@check50.check(compiles)
def test9():
    """everything is VERY STRONG"""
    check50.run("java PasswordRater").stdin("Bkx4UHM@$#g5zZ4etd2V").stdout("VERY STRONG\n").exit()
