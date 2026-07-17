import check50
from re import match

@check50.check()
def exists():
    """readability.py exists."""
    check50.exists("readability.py")

@check50.check(exists)
def multiple_sentences():
    """handles multiple sentences"""
    check50.include("texts")
    check50.run("python3 readability.py texts/rowling_excerpt.txt").stdout("Grade\D+5", "Grade 5\n").exit(0)

@check50.check(exists, max_log_lines=100)
def multiple_lines():
    """handles multiple lines of input"""
    check50.include("texts")
    check50.run("python3 readability.py texts/textbook_excerpt.txt").stdout("Grade\D+11", "Grade 11\n").exit(0)

@check50.check(exists)
def long_text():
    """handles a long text"""
    check50.include("texts")
    check50.run("python3 readability.py texts/carroll.txt").stdout("Grade\D+7", "Grade 7\n").exit(0)

@check50.check(exists)
def short_gutenberg_text():
    """handles a short text from Gutenberg by avoiding reading past "*** END" """
    check50.include("texts")
    output = check50.run("python3 readability.py texts/potter.txt").stdout()
    expected = "Grade 7\n"
    help = None
    if output == "Grade 11\n":
        help = "\n\tMake sure you don't read the long license at the bottom of potter.txt\n\tIt's a much higher reading level than the text itself!"
        raise check50.Mismatch(expected, output, help=help)

    if not match(expected, output):
        raise check50.Mismatch(expected, output, help=help)

@check50.check(exists)
def test_reject_nofile():
    """demands a file passed in"""
    check50.run("python3 readability.py").exit()