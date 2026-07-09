import check50

@check50.check()
def exists():
    """personalized_hello.py exists"""
    check50.exists("personalized_hello.py")

@check50.check(exists)
def testalice():
    """input of Alice yields output of Hello, Alice!"""
    check50.run("python3 indoor.py").stdin("Alice", prompt=False).stdout("Hello, Alice!").exit()

@check50.check(exists)
def testbob():
    """input of Bob yields output of Hello, Bob!"""
    check50.run("python3 indoor.py").stdin("Bob", prompt=False).stdout("Hello, Bob!").exit()
