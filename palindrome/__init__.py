import check50

@check50.check()
def exists():
    """palindrome.py exists"""
    check50.exists("palindrome.py")

@check50.check(exists)
def testaibohphobia():
    """input of aibohphobia yields output of Palindrome"""
    check50.run("python3 palindrome.py").stdin("aibohphobia").stdout("Palindrome").exit()

@check50.check(exists)
def testnoon():
    """input of noon yields output of Palindrome"""
    check50.run("python3 palindrome.py").stdin("noon").stdout("Palindrome").exit()

@check50.check(exists)
def testnoonmixed():
    """input of NOon yields output of Palindrome"""
    check50.run("python3 palindrome.py").stdin("NOon").stdout("Palindrome").exit()

@check50.check(exists)
def testtacocat():
    """input of tacocat yields output of Palindrome"""
    check50.run("python3 palindrome.py").stdin("tacocat").stdout("Palindrome").exit()

@check50.check(exists)
def testpalindrome():
    """input of palindrome yields output starting with No"""
    check50.run("python3 palindrome.py").stdin("palindrome").stdout("No").exit()