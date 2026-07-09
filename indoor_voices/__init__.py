import check50

@check50.check()
def exists():
    """indoor_voices.py exists"""
    check50.exists("indoor_voices.py")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("python3 indoor_voices.py").stdin("HELLO", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """input of THIS IS POLY CS yields output of this is poly cs"""
    check50.run("python3 indoor_voices.py").stdin("THIS IS POLY CS", prompt=False).stdout("this is poly cs").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 indoor_voices.py").stdin("50", prompt=False).stdout("50").exit()