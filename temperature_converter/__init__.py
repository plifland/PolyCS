import check50

@check50.check()
def exists():
    """temperature_converter.py exists"""
    check50.exists("temperature_converter.py")

@check50.check(exists)
def testzero():
    """input of 0 yields output of Fahrenheit temperature: 32"""
    check50.run("python3 temperature_converter.py").stdin("0", prompt=True).stdout("Fahrenheit temperature: 32").exit()

@check50.check(exists)
def testroundup():
    """input of 42 yields output of Fahrenheit temperature: 108"""
    check50.run("python3 temperature_converter.py").stdin("42", prompt=True).stdout("Fahrenheit temperature: 108").exit()

@check50.check(exists)
def testrounddown():
    """input of 9 yields output of Fahrenheit temperature: 48"""
    check50.run("python3 temperature_converter.py").stdin("9", prompt=True).stdout("Fahrenheit temperature: 48").exit()