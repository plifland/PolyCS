import check50

@check50.check()
def exists():
    """Palindrome.java exists"""
    check50.exists("Palindrome.java")

@check50.check(exists)
def compiles():
    """Palindrome.java compiles"""
    check50.run("javac Palindrome.java").exit(0)

@check50.check(compiles)
def testaibohphobia():
    """input of aibohphobia yields output of Palindrome"""
    check50.run("java Palindrome").stdin("aibohphobia").stdout("Palindrome").exit()

@check50.check(compiles)
def testnoon():
    """input of noon yields output of Palindrome"""
    check50.run("java Palindrome").stdin("noon").stdout("Palindrome").exit()

@check50.check(compiles)
def testnoonmixed():
    """input of NOon yields output of Palindrome"""
    check50.run("java Palindrome").stdin("NOon").stdout("Palindrome").exit()

@check50.check(compiles)
def testtacocat():
    """input of tacocat yields output of Palindrome"""
    check50.run("java Palindrome").stdin("tacocat").stdout("Palindrome").exit()

@check50.check(compiles)
def testpalindrome():
    """input of palindrome yields output starting with No"""
    check50.run("java Palindrome").stdin("palindrome").stdout("No").exit()