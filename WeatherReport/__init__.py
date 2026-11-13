import check50

@check50.check()
def exists():
    """WeatherReport.java exists."""
    check50.exists("WeatherReport.java")

@check50.check(exists)
def compiles():
    """WeatherReport.java compiles"""
    check50.run("javac WeatherReport.java").exit(0)

@check50.check(compiles)
def testClean():
    """Data cleaning"""
    check50.run("java WeatherReport").stdin("Cleaning").stdout("Cleaned data\n\[83, 82, 85, 85, 84, 82, 81, 80, 83, 91, 90, 93, 88, 88, 88, 86, 83, 79, 78, 81, 80, 85, 86, 85, 86, 81, 81, 75, 78, 72, 77, 83, 86, 92, 89, 90, 92, 92, 92, 87, 91, 84, 90, 94, 99, 95, 91, 93, 95, 95, 93, 90, 95, 96, 98, 96, 95, 93, 91, 93, 98, 98, 97, 94, 90, 91, 94, 96, 97, 97, 94, 94, 91, 86, 87, 88, 90, 93, 98, 99, 97, 99, 100, 104, 102, 100, 103, 95, 99, 99, 95, 90\]\n\[60, 60, 58, 60, 63, 63, 61, 62, 60, 63, 65, 64, 64, 63, 63, 61, 60, 60, 60, 56, 57, 59, 61, 61, 60, 60, 62, 62, 61, 62, 60, 59, 58, 60, 66, 65, 64, 64, 64, 64, 65, 66, 68, 68, 71, 70, 68, 69, 68, 68, 70, 71, 70, 71, 70, 71, 70, 67, 68, 68, 65, 68, 68, 67, 66, 67, 68, 70, 69, 71, 73, 70, 67, 67, 67, 65, 65, 66, 70, 69, 68, 73, 72, 73, 73, 72, 77, 76, 76, 75, 72, 67\]\n\n").exit()

@check50.check(compiles)
def test90Streak():
    """90-streak"""
    check50.run("java WeatherReport").stdin("90-streak").stdout("Longest streak of 90 degree temperatures: 31 days\n\n").exit()

@check50.check(compiles)
def test100Streak():
    """100-streak"""
    check50.run("java WeatherReport").stdin("100-streak").stdout("Longest streak of 100 degree temperatures: 5 days\n\n").exit()

@check50.check(compiles)
def test70Streak():
    """70-streak"""
    check50.run("java WeatherReport").stdin("70-streak").stdout("Longest streak of 70 degree temperatures: 92 days\n\n").exit()

@check50.check(compiles)
def testAvgDailySpread():
    """AvgDailySpread"""
    check50.run("java WeatherReport").stdin("AvgDailySpread").stdout("Average daily temperature spread: 24.3 degrees\n").exit()

@check50.check(compiles)
def testMaxVolatility():
    """MaxVolatility"""
    check50.run("java WeatherReport").stdin("MaxVolatility").stdout("Largest change in high temperature between two days: 8 degrees\n\n").exit()

@check50.check(compiles)
def testAvgVolatility():
    """AvgVolatility"""
    check50.run("java WeatherReport").stdin("AvgVolatility").stdout("Average change in high temperature between two days: 2.7 degrees\n").exit()