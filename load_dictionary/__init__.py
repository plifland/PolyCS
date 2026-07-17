import check50

@check50.check()
def exists():
    """load_dictionary.py exists."""
    check50.exists("load_dictionary.py")

@check50.check(exists)
def load_small():
    """successfully loads a small dictionary"""
    check50.include("small")
    check50.run("python3 load_dictionary.py small/dict.txt").stdout(open("small/out.txt").read()).exit(0)

@check50.check(exists)
def load_large():
    """successfully loads a large dictionary"""
    check50.include("large")
    check50.run("python3 load_dictionary.py large/dict.txt").stdout(open("large/out.txt").read()).exit(0)

@check50.check(exists)
def test_reject_nofile():
    """demands a file passed in via command line"""
    check50.run("python3 load_dictionary.py").stdout("usage: load_dictionary.py .+", regex=True).exit(0)