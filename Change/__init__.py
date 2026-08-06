import check50


@check50.check()
def exists():
    """Change.java exists"""
    check50.exists("Change.java")

@check50.check(exists)
def compiles():
    """Change.java compiles"""
    check50.run("javac Change.java").exit()

@check50.check(compiles)
def test041():
    """input of 41 yields output of 4"""
    check50.run("java Change").stdin("41").stdout(coins(4), "4\n").exit()

@check50.check(compiles)
def test001():
    """input of 1 yields output of 1"""
    check50.run("java Change").stdin("1").stdout(coins(1), "1\n").exit()

@check50.check(compiles)
def test015():
    """input of 15 yields output of 2"""
    check50.run("java Change").stdin("15").stdout(coins(2), "2\n").exit()

@check50.check(compiles)
def test160():
    """input of 160 yields output of 7"""
    check50.run("java Change").stdin("160").stdout(coins(7), "7\n").exit()

@check50.check(compiles)
def test230():
    """input of 2300 yields output of 92"""
    check50.run("java Change").stdin("2300").stdout(coins(92), "92\n").exit()

@check50.check(compiles)
def test420():
    """input of 420 yields output of 18"""
    from re import search
    expected = "18\n"
    actual = check50.run("java Change").stdin("420").stdout()
    if not search(coins(18), actual):
        help = None
        if search(coins(22), actual):
            help = "did you forget to round your input to the nearest cent?"
        raise check50.Mismatch(expected, actual, help=help)

@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("java Change").stdin("-1").reject()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("java Change").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("java Change").stdin("").reject()


def coins(num):
    return fr"(^|[^\d]){num}(?!\d)"