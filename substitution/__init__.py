import check50

@check50.check()
def exists():
    """substitution.py exists."""
    check50.exists("substitution.py")

@check50.check(exists)
def encrypt1():
    """encrypts "A" as "Z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("python3 substitution.py").stdin("A").stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA").stdout(
        "[Cc]iphertext:\s*Z\n.*", "ciphertext: Z\n"
    ).exit(0)

@check50.check(exists)
def encrypt2():
    """encrypts "a" as "z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("python3 substitution.py").stdin("a").stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA").stdout(
        "[Cc]iphertext:\s*z\n.*", "ciphertext: z\n"
    ).exit(0)

@check50.check(exists)
def encrypt3():
    """encrypts "ABC" as "NJQ" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("python3 substitution.py").stdin("ABC").stdin("NJQSUYBRXMOPFTHZVAWCGILKED").stdout(
        "[Cc]iphertext:\s*NJQ\n.*", "ciphertext: NJQ\n"
    ).exit(0)

@check50.check(exists)
def encrypt4():
    """encrypts "XyZ" as "KeD" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("python3 substitution.py").stdin("XyZ").stdin("NJQSUYBRXMOPFTHZVAWCGILKED").stdout(
        "[Cc]iphertext:\s*KeD\n.*", "ciphertext: KeD\n"
    ).exit(0)

@check50.check(exists)
def encrypt5():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using YUKFRNLBAVMWZTEOGXHCIPJSQD as key"""
    check50.run("python3 substitution.py").stdin("This is CS2026").stdin("YUKFRNLBAVMWZTEOGXHCIPJSQD").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(exists)
def encrypt6():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using yukfrnlbavmwzteogxhcipjsqd as key"""
    check50.run("python3 substitution.py").stdin("This is CS2026").stdin("yukfrnlbavmwzteogxhcipjsqd").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(exists)
def encrypt7():
    """encrypts "This is CS2026" as "Cbah ah KH2026" using YUKFRNLBAVMWZteogxhcipjsqd as key"""
    check50.run("python3 substitution.py").stdin("This is CS2026").stdin("YUKFRNLBAVMWZteogxhcipjsqd").stdout(
        "[Cc]iphertext:\s*Cbah ah KH2026\n.*", "ciphertext: Cbah ah KH2026\n"
    ).exit(0)

@check50.check(exists)
def encrypt8():
    """encrypts all alphabetic characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("python3 substitution.py").stdin(
        "The quick brown fox jumps over the lazy dog"
    ).stdin("DWUSXNPQKEGCZFJBTLYROHIAVM").stdout(
        "[Cc]iphertext:\s*Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n.*", "ciphertext: Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n"
    ).exit(0)

@check50.check(exists)
def encrypt9():
    """does not encrypt non-alphabetical characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("python3 substitution.py").stdin("Shh... Don't tell!").stdin("DWUSXNPQKEGCZFJBTLYROHIAVM").stdout(
        "[Cc]iphertext:\s*Yqq... Sjf'r rxcc!\n.*", "ciphertext: Yqq... Sjf'r rxcc!\n"
    ).exit(0)

@check50.check(exists)
def handles_empty_key():
    """handles empty key"""
    check50.run("python3 substitution.py").stdin("this key is empty").stdin("").reject()

@check50.check(exists)
def handles_short_key():
    """handles too short key"""
    check50.run("python3 substitution.py").stdin("this key is short").stdin("asdf").reject()

@check50.check(exists)
def handles_long_key():
    """handles too long key"""
    check50.run("python3 substitution.py").stdin("this key is long").stdin("thisisthekeythatneverendsyesitgoesonandonmyfriends").reject()

@check50.check(exists)
def handles_nonalpha_key():
    """handles non-alpha key"""
    check50.run("python3 substitution.py").stdin("this key is bad").stdin("ZYXWVUTSRQPONMLKJIHG123CBA").reject()

@check50.check(exists)
def handles_key_with_repeat_letters():
    """handles repeating key"""
    check50.run("python3 substitution.py").stdin("this key repeats").stdin("AAAAAAAAAAAAAAAAAAAAAAAAA").reject()
