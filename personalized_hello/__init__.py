import check50

@check50.check()
def exists():
    """personalized_hello.py exists"""
    check50.exists("personalized_hello.py")

@check50.check(exists)
def testalice():
    """input of Alice yields output of Hello, Alice!"""
    check50.run("python3 personalized_hello.py").stdin("Alice", prompt=True).stdout("Hello, Alice!").exit()

@check50.check(exists)
def testbob():
    """input of Bob yields output of Hello, Bob!"""
    check50.run("python3 personalized_hello.py").stdin("Bob", prompt=True).stdout("Hello, Bob!").exit()
