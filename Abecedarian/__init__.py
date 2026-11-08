import check50

@check50.check()
def exists():
    """Abecedarian.java exists"""
    check50.exists("Abecedarian.java")

@check50.check(exists)
def compiles():
    """Abecedarian.java compiles"""
    check50.run("javac Abecedarian.java").exit(0)

@check50.check(compiles)
def testbiopsy():
    """input of biopsy yields output of Abecedarian"""
    check50.run("java Abecedarian").stdin("biopsy").stdout("Abecedarian").exit()

@check50.check(compiles)
def testannoy():
    """input of annoy yields output of Abecedarian"""
    check50.run("java Abecedarian").stdin("annoy").stdout("Abecedarian").exit()

@check50.check(compiles)
def testannoymixed():
    """input of anNOy yields output of Abecedarian"""
    check50.run("java Abecedarian").stdin("anNOy").stdout("Abecedarian").exit()

@check50.check(compiles)
def testtacocat():
    """input of tacocat yields output of Abecedarian"""
    check50.run("java Abecedarian").stdin("tacocat").stdout("No").exit()

@check50.check(compiles)
def testabecedarian():
    """input of abecedarian yields output starting with No"""
    check50.run("java Abecedarian").stdin("abecedarian").stdout("No").exit()