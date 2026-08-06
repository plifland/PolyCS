import check50

@check50.check()
def exists():
    """DogsVsCats.java exists"""
    check50.exists("DogsVsCats.java")

@check50.check(exists)
def compiles():
    """DogsVsCats.java compiles"""
    check50.run("javac DogsVsCats.java").exit()

@check50.check(compiles)
def testyes():
    """output starts with "Dog food ad:" on a "yes" input"""
    check50.run("java DogsVsCats").stdin("yes").stdout("Dog food ad:.+", regex=True).exit()

@check50.check(compiles)
def testcase():
    """output starts with "Dog food ad:" on a "YEs" input"""
    check50.run("java DogsVsCats").stdin("YEs").stdout("Dog food ad:.+", regex=True).exit()

@check50.check(compiles)
def testno():
    """output starts with "Cat food ad:" on a "no" input"""
    check50.run("java DogsVsCats").stdin("no").stdout("Cat food ad:.+", regex=True).exit()

@check50.check(compiles)
def testnonsense():
    """output starts with "Cat food ad:" on "gerbils4life" input"""
    check50.run("java DogsVsCats").stdin("gerbils4life").stdout("Cat food ad:.+", regex=True).exit()

@check50.check(compiles)
def testempty():
    """output starts with "Cat food ad:" on an empty input"""
    check50.run("java DogsVsCats").stdin("").stdout("Cat food ad:.+", regex=True).exit()