import check50

@check50.check()
def exists():
    """IndoorVoices.java exists"""
    check50.exists("IndoorVoices.java")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("java IndoorVoices.java").stdin("HELLO").stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """input of THIS is POLY CS yields output of this is poly cs"""
    check50.run("java IndoorVoices.java").stdin("THIS is POLY CS").stdout("this is poly cs").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("java IndoorVoices.java").stdin("50").stdout("50").exit()