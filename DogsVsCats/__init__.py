import check50

@check50.check()
def exists():
    """DogsVsCats.java exists"""
    check50.exists("DogsVsCats.java")

@check50.check(exists)
def testyes():
    """output starts with "Dog food ad:" on a "yes" input"""
    check50.run("java DogsVsCats.java").stdin("yes", timeout=10).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def testcase():
    """output starts with "Dog food ad:" on a "YEs" input"""
    check50.run("java DogsVsCats.java").stdin("YEs", timeout=10).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def testno():
    """output starts with "Cat food ad:" on a "no" input"""
    check50.run("java DogsVsCats.java").stdin("no", timeout=10).stdout("Cat food ad:.+", regex=True).exit()

@check50.check(exists)
def testnonsense():
    """output starts with "Cat food ad:" on a nonsense input"""
    check50.run("java DogsVsCats.java").stdin("gerbils4life", timeout=10).stdout("Cat food ad:.+", regex=True).exit()

@check50.check(exists)
def testempty():
    """output starts with "Cat food ad:" on an empty input"""
    check50.run("java DogsVsCats.java").stdin("", timeout=10).stdout("Cat food ad:.+", regex=True).exit()