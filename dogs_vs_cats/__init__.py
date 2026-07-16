import check50

@check50.check()
def exists():
    """dogs_vs_cats.py exists"""
    check50.exists("dogs_vs_cats.py")

@check50.check(exists)
def testyes():
    """output starts with "Dog food ad:" on a "yes" input"""
    check50.run("python3 dogs_vs_cats.py").stdin("yes", prompt=True).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def testcase():
    """output starts with "Dog food ad:" on a "YEs" input"""
    check50.run("python3 dogs_vs_cats.py").stdin("YEs", prompt=True).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def testno():
    """output starts with "Cat food ad:" on a "no" input"""
    check50.run("python3 dogs_vs_cats.py").stdin("no", prompt=True).stdout("Cat food ad:.+", regex=True).exit()

@check50.check(exists)
def testnonsense():
    """output starts with "Cat food ad:" on a nonsense input"""
    check50.run("python3 dogs_vs_cats.py").stdin("gerbils4life", prompt=True).stdout("Cat food ad:.+", regex=True).exit()

@check50.check(exists)
def testempty():
    """output starts with "Cat food ad:" on an empty input"""
    check50.run("python3 dogs_vs_cats.py").stdin("", prompt=True).stdout("Cat food ad:.+", regex=True).exit()