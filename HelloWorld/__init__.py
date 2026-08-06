import check50

@check50.check()
def exists():
    """HelloWorld.java exists"""
    check50.exists("HelloWorld.java")

@check50.check(exists)
def compiles():
    """HelloWorld.java compiles"""
    check50.run("javac HelloWorld.java").exit(0)

@check50.check(compiles)
def testhello():
    """output is Hello, world!"""
    check50.run("java HelloWorld").stdout("Hello, world!", regex=False).exit()

