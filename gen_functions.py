import secrets
import string

char_dictionary = {
    'gen_hexacosa': 'Random alphabetical & numerical character(s)',
    'gen_nonalpha': 'Random special character(s) & digit(s)',
    'gen_num': 'Random digit(s)',
    'gen_hexadec': 'Random hexidecimal character(s)',
    'gen_punc': 'Random special character(s)',
    # 'gen_alpha': 'Alphabet',
    'gen_spchar': 'Random special character(s)'
    # 'gen_all': 'Alphabet + Digits 0-9 + Special Characters'
}


# gen two characters with random digits + alpha
def gen_hexacosa(N):
    hexacosa = string.ascii_letters + string.digits
    return ''.join(secrets.choice(hexacosa) for n in range(0, N))


# gen three characters with special characters + digits
def gen_nonalpha(N):
    nonalpha = string.digits + string.punctuation
    return ''.join(secrets.choice(nonalpha) for n in range(0, N))


def gen_num(N):
    num = string.digits
    return ''.join(secrets.choice(num) for n in range(0, N))


def gen_spchar(N):
    special = string.punctuation    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    return ''.join(secrets.choice(special) for n in range(0, N))


def gen_hexadec(N):
    hexadec = string.hexdigits
    return ''.join(secrets.choice(hexadec) for n in range(0, N))


def gen_punc(N):
    special = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    lst = ['{', '}', "|", '[', ']', '/', '(', ')', '\\', '`', ',']
    for x in lst:
        special = special.replace(x, '')
    return ''.join(secrets.choice(special) for n in range(0, N))
