import check50

@check50.check()
def exists():
    """TemperatureConverter.java exists"""
    check50.exists("TemperatureConverter.java")

@check50.check(exists)
def testzero():
    """input of 0 yields output of 32"""
    check50.run("java TemperatureConverter.java").stdin("0").stdout("32").exit()

@check50.check(exists)
def testtruncate():
    """input of 42 yields output of 107"""
    check50.run("java TemperatureConverter.java").stdin("42").stdout("107").exit()

@check50.check(exists)
def testrounddown():
    """input of 9 yields output of 48"""
    check50.run("java TemperatureConverter.java").stdin("9").stdout("48").exit()