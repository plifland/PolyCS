import check50

@check50.check()
def exists():
    """PersonalHello.java exists"""
    check50.exists("PersonalHello.java")
    check50.include("Panther.txt", "Poly Panther.txt")

@check50.check(exists)
def test1():
    """handles a 1 word name correctly """
    out = check50.run("java ./PersonalHello.java").stdin("P").stdout()
    check_output(out, open("Panther.txt").read())

@check50.check(exists)
def test2():
    """handles a name with a space correctly """
    out = check50.run("java ./PersonalHello.java").stdin("Poly Panther").stdout()
    check_output(out, open("Poly Panther.txt").read())


def check_output(output, correct):
    if output.splitlines() == correct.splitlines():
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = output.splitlines()
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)