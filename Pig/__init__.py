import check50

@check50.check()
def exists():
    """Pig.java exists."""
    check50.exists("Pig.java")

@check50.check(exists)
def compiles():
    """Pig.java compiles"""
    check50.run("javac Pig.java").exit(0)
