import check50

@check50.check()
def exists():
    """PersonalizedAds.java exists"""
    check50.exists("PersonalizedAds.java")

@check50.check(exists)
def compiles():
    """PersonalizedAds.java compiles"""
    check50.run("javac PersonalizedAds.java").exit(0)

