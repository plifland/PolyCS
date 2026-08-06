import check50

@check50.check()
def exists():
    """BoulderLibrary.java exists"""
    check50.exists("BoulderLibrary.java")

@check50.check(exists)
def compiles():
    """BoulderLibrary.java compiles"""
    check50.run("javac BoulderLibrary.java")

@check50.check(compiles)
def testfancy():
    """Serves a fancy fundraiser ad for a boulder resident over 24"""
    check50.run("java ./BoulderLibrary").stdin("80301", prompt=False).stdin("40", prompt=False).stdout("Fancy fundraiser ad:.+").exit()

@check50.check(compiles)
def test25():
    """Serves a fancy fundraiser ad for a boulder resident exactly 25"""
    check50.run("java BoulderLibrary").stdin("80302", prompt=False).stdin("25", prompt=False).stdout("Fancy fundraiser ad:.+").exit()

@check50.check(compiles)
def testevent():
    """Serves a library event ad for a boulder resident under 25"""
    check50.run("java ./BoulderLibrary").stdin("80310", timeout=10).stdin("17").stdout("Library event ad:.+").exit()

@check50.check(compiles)
def testtourist():
    """Serves a tourist ad for a non-boulder resident"""
    check50.run("java BoulderLibrary").stdin("91106", timeout=10).stdin("17").stdout("Tourist ad:.+").exit()
