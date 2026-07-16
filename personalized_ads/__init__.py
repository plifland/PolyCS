import check50

@check50.check()
def exists():
    """hello_world.py exists"""
    check50.exists("hello_world.py")

@check50.check(exists)
def testhello():
    """output is Hello, world!"""
    check50.run("python3 hello_world.py").stdout("Hello, world!").exit()

