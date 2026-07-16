import check50

@check50.check()
def exists():
    """dogs_vs_cats.py exists"""
    check50.exists("dogs_vs_cats.py")

@check50.check(exists)
def testyes():
    """output starts with Dog food ad: on a yes"""
    check50.run("python3 dogs_vs_cats.py").stdin("yes", prompt=False).stdout("Dog food ad:.+", regex=True).exit()

def testYEs():
    """output starts with Dog food ad: on a YEs"""
    check50.run("python3 dogs_vs_cats.py").stdin("YEs", prompt=False).stdout("Dog food ad:.+", regex=True).exit()

def testno():
    """output starts with Cat food ad: on a no"""
    check50.run("python3 dogs_vs_cats.py").stdin("no", prompt=False).stdout("Cat food ad:.+", regex=True).exit()

def testnonsense():
    """output starts with Cat food ad: on a random input"""
    check50.run("python3 dogs_vs_cats.py").stdin("gerbils4life", prompt=False).stdout("Cat food ad:.+", regex=True).exit()

def testempty():
    """output starts with Cat food ad: on an empty input"""
    check50.run("python3 dogs_vs_cats.py").stdin("", prompt=False).stdout("Cat food ad:.+", regex=True).exit()