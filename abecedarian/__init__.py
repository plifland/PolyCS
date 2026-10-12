import check50

@check50.check()
def exists():
    """abecedarian.py exists"""
    check50.exists("abecedarian.py")

@check50.check(exists)
def testbiopsy():
    """input of biopsy yields output of Abecedarian"""
    check50.run("python3 abecedarian.py").stdin("biopsy").stdout("Abecedarian").exit()

@check50.check(exists)
def testannoy():
    """input of annoy yields output of Abecedarian"""
    check50.run("python3 abecedarian.py").stdin("annoy").stdout("Abecedarian").exit()

@check50.check(exists)
def testannoymixed():
    """input of anNOy yields output of Abecedarian"""
    check50.run("python3 abecedarian.py").stdin("anNOy").stdout("Abecedarian").exit()

@check50.check(exists)
def testtacocat():
    """input of tacocat yields output of Abecedarian"""
    check50.run("python3 abecedarian.py").stdin("tacocat").stdout("No").exit()

@check50.check(exists)
def testabecedarian():
    """input of abecedarian yields output starting with No"""
    check50.run("python3 abecedarian.py").stdin("abecedarian").stdout("No").exit()
