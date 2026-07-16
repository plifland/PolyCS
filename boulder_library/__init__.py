import check50

@check50.check()
def exists():
    """boulder_library.py exists"""
    check50.exists("boulder_library.py")

@check50.check(exists)
def testfancy():
    """Serves a fancy fundraiser ad for a boulder resident over 24"""
    check50.run("python3 boulder_library.py").stdin("80301", prompt=True).stdin("40", prompt=True).stdout("Fancy fundraiser ad:.+", regex=True).exit()

@check50.check(exists)
def test25():
    """Serves a fancy fundraiser ad for a boulder resident exactly 25"""
    check50.run("python3 boulder_library.py").stdin("80302", prompt=True).stdin("25", prompt=True).stdout("Fancy fundraiser ad:.+", regex=True).exit()

@check50.check(exists)
def testevent():
    """Serves a library event ad for a boulder resident under 25"""
    check50.run("python3 boulder_library.py").stdin("80310", prompt=True).stdin("17", prompt=True).stdout("Library event ad:.+", regex=True).exit()

@check50.check(exists)
def testtourist():
    """Serves a tourist ad for a non-boulder resident"""
    check50.run("python3 boulder_library.py").stdin("91106", prompt=True).stdin("17", prompt=True).stdout("Tourist ad:.+", regex=True).exit()
