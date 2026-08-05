import check50

@check50.check()
def exists():
    """HelloWorld.java exists"""
    check50.exists("HelloWorld.java")

@check50.check(exists)
def testhello():
    """output is Hello, world!"""
    check50.run("java HelloWorld.java").stdout("Hello, world!").exit()

