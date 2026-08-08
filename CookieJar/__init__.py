import check50

@check50.check()
def exists_jar():
    """CookieJar.java exists."""
    check50.exists("CookieJar.java")

@check50.check()
def exists_client():
    """MysteriousBlueClient.java exists."""
    check50.exists("MysteriousBlueClient.java")

@check50.check(exists)
def compiles_jar():
    """CookieJar.java compiles"""
    check50.run("javac CookieJar.java").exit(0)

@check50.check(exists)
def compiles_client():
    """MysteriousBlueClient.java compiles"""
    check50.run("javac MysteriousBlueClient.java").exit(0)
