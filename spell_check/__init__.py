import check50

@check50.check()
def exists():
    """spell_check.py exists."""
    check50.exists("spell_check.py")

@check50.check(exists)
def basic():
    """handles most basic words properly"""
    check50.include("basic")
    check50.run("python3 spell_check.py basic/dict basic/text").stdout("2 misspelled words\n").exit()

@check50.check(exists)
def min_length():
    """handles min length (1-char) words"""
    check50.include("min_length")
    check50.run("python3 spell_check.py min_length/dict min_length/text").stdout("3 misspelled words\n").exit()

@check50.check(exists)
def apostrophe():
    """handles words with apostrophes properly"""
    check50.include("apostrophe")
    check50.run("python3 spell_check.py apostrophe/dict apostrophe/text").stdout("2 misspelled words\n").exit()

@check50.check(exists)
def cases():
    """handles words with upper and lower letters properly"""
    check50.include("cases")
    check50.run("python3 spell_check.py cases/dict cases/text").stdout("0 misspelled words\n").exit()

@check50.check(exists)
def substring():
    """handles when one word contains another valid word"""
    check50.include("substring")
    check50.run("python3 spell_check.py substring/dict substring/text").stdout("4 misspelled words\n").exit()

@check50.check(exists)
def substring():
    """handles large dictionary"""
    check50.include("large")
    check50.run("python3 spell_check.py large/dict large/text").stdout("0 misspelled words\n").exit()

@check50.check(exists)
def test_reject_nofile():
    """demands a file passed in via command line"""
    check50.run("python3 spell_check.py").stdout("usage: spell_check.py .+", regex=True).exit()