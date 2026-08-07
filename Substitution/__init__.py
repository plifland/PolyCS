import check50

@check50.check()
def exists():
    """Substitution.java exists."""
    check50.exists("Substitution.java")

@check50.check(exists)
def compiles():
    """Substitution.java compiles"""
    check50.run("javac Substitution.java").exit(0)

@check50.check(compiles)
def encrypt1():
    """encrypts "A" as "Z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("java Substitution").stdin("A").stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA").stdout(
        "[Cc]iphertext:\s*Z\n.*", "ciphertext: Z\n"
    ).exit(0)

@check50.check(compiles)
def encrypt2():
    """encrypts "a" as "z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("java Substitution").stdin("a").stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA").stdout(
        "[Cc]iphertext:\s*z\n.*", "ciphertext: z\n"
    ).exit(0)

@check50.check(compiles)
def encrypt3():
    """encrypts "ABC" as "NJQ" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("java Substitution").stdin("ABC").stdin("NJQSUYBRXMOPFTHZVAWCGILKED").stdout(
        "[Cc]iphertext:\s*NJQ\n.*", "ciphertext: NJQ\n"
    ).exit(0)

@check50.check(compiles)
def encrypt4():
    """encrypts "XyZ" as "KeD" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("java Substitution").stdin("XyZ").stdin("NJQSUYBRXMOPFTHZVAWCGILKED").stdout(
        "[Cc]iphertext:\s*KeD\n.*", "ciphertext: KeD\n"
    ).exit(0)

@check50.check(compiles)
def encrypt5():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using YUKFRNLBAVMWZTEOGXHCIPJSQD as key"""
    check50.run("java Substitution").stdin("This is CS2026").stdin("YUKFRNLBAVMWZTEOGXHCIPJSQD").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(compiles)
def encrypt6():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using yukfrnlbavmwzteogxhcipjsqd as key"""
    check50.run("java Substitution").stdin("This is CS2026").stdin("yukfrnlbavmwzteogxhcipjsqd").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(compiles)
def encrypt7():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using YUKFRNLBAVMWZteogxhcipjsqd as key"""
    check50.run("java Substitution").stdin("This is CS2026").stdin("YUKFRNLBAVMWZteogxhcipjsqd").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(compiles)
def encrypt8():
    """encrypts all alphabetic characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("java Substitution").stdin(
        "The quick brown fox jumps over the lazy dog"
    ).stdin("DWUSXNPQKEGCZFJBTLYROHIAVM").stdout(
        "[Cc]iphertext:\s*Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n.*", "ciphertext: Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n"
    ).exit(0)

@check50.check(compiles)
def encrypt9():
    """does not encrypt non-alphabetical characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("java Substitution").stdin("Shh... Don't tell!").stdin("DWUSXNPQKEGCZFJBTLYROHIAVM").stdout(
        "[Cc]iphertext:\s*Yqq... Sjf'r rxcc!\n.*", "ciphertext: Yqq... Sjf'r rxcc!\n"
    ).exit(0)

@check50.check(compiles)
def handles_empty_key():
    """handles empty key"""
    check50.run("java Substitution").stdin("this key is empty").stdin("").reject()

@check50.check(compiles)
def handles_short_key():
    """handles too short key"""
    check50.run("java Substitution").stdin("this key is short").stdin("asdf").reject()

@check50.check(compiles)
def handles_long_key():
    """handles too long key"""
    check50.run("java Substitution").stdin("this key is long").stdin("thisisthekeythatneverendsyesitgoesonandonmyfriends").reject()

@check50.check(compiles)
def handles_nonalpha_key():
    """handles non-alpha key"""
    check50.run("java Substitution").stdin("this key is bad").stdin("ZYXWVUTSRQPONMLKJIHG123CBA").reject()

@check50.check(compiles)
def handles_key_with_repeat_letters():
    """handles repeating key"""
    check50.run("java Substitution").stdin("this key repeats").stdin("AAAAAAAAAAAAAAAAAAAAAAAAA").reject()
