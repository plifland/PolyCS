import check50

@check50.check()
def exists():
    """readability.py exists."""
    check50.exists("readability.py")

@check50.check(exists)
def multiple_sentences():
    """handles multiple sentences"""
    check50.run("python3 readability.py texts/rowling_excerpt.txt").stdout("Grade\D+5", "Grade 5\n").exit(0)

@check50.check(exists)
def multiple_lines():
    """handles mulitple lines of input"""
    check50.run("python3 readability.py texts/textbook_excerpt.txt").stdout("Grade\D+11", "Grade 11\n").exit(0)

@check50.check(exists)
def long_text():
    """handles a long text"""
    check50.run("python3 readability.py texts/carroll.txt").stdout("Grade\D+7", "Grade 7\n").exit(0)

@check50.check(exists)
def short_gutenberg_text():
    """handles a short text from Gutenberg by avoiding reading under *** END"""
    output = check50.run("python3 readability.py texts/potter.txt").stdout("Grade\D+7", "Grade 7\n")
    if output == "Grade 11":
      help = "make sure you don't read the long license at the bottom of potter.txt!\nIt's a much higher reading level than the text itself!"
      raise check50.Mismatch("Grade 7\n", output, help=help)

