import check50

@check50.check()
def exists():
    """Caesar.java exists."""
    check50.exists("Caesar.java")

@check50.check(exists)
def compiles():
    """Caesar.java compiles"""
    check50.run("javac Caesar.java").exit(0)

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("java Caesar").stdin("a").stdin("1").stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("java Caesar").stdin("barfoo").stdin("23").stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("java Caesar").stdin("BARFOO").stdin("3").stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("java Caesar").stdin("BaRFoo").stdin("4").stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    check50.run("java Caesar").stdin("barfoo").stdin("65").stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("java Caesar").stdin("world, say hello!").stdin("12").stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_empty_key():
    """handles empty key"""
    check50.run("java Caesar").stdin("this key is empty").stdin("").reject()

@check50.check(compiles)
def handles_nonnumeric_key():
    """handles non-numeric key"""
    check50.run("java Caesar").stdin("this key is bad").stdin("bad to the bone").reject()
