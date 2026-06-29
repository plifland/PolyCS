import check50
import check50.c

@check50.check()
def exists():
    """PersonalHello.java exists"""
    check50.exists("PersonalHello.java")
    check50.include("Panther.txt", "Poly Panther.txt")

@check50.check(exists)
def compiles():
    """PersonalHello.java compiles"""
    check50.c.compile("PersonalHello.java", lcs50=True)

@check50.check(compiles)
def test1():
    """handles a 1 word name correctly """
    out = check50.run("./PersonalHello.java").stdin("Poly").stdout()
    check_output(out, open("Panther.txt").read())

@check50.check(compiles)
def test2():
    """handles a name with a space correctly """
    out = check50.run("./PersonalHello.java").stdin("Poly Panther").stdout()
    check_output(out, open("Poly Panther.txt").read())


def check_output(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)