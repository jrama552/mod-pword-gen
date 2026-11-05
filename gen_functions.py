import secrets
import string

char_dictionary = {
    'random_alphanumeric': 'Random alphabetical & numerical character(s)',
    'random_digits_and_punctuation': 'Random special character(s) & digit(s)',
    'random_digits': 'Random digit(s)',
    'random_hex': 'Random hexidecimal character(s)',
    'random_safe_punctuation': 'Random special character(s)',
    # 'gen_alpha': 'Alphabet',
    'random_punctuation': 'Random special character(s)'
    # 'gen_all': 'Alphabet + Digits 0-9 + Special Characters'
}


# gen two characters with random digits + alpha
def random_alphanumeric(N):  # Returns a string of N random letters/digits
    hexacosa = string.ascii_letters + string.digits
    return ''.join(secrets.choice(hexacosa) for n in range(0, N))


# gen three characters with special characters + digits
def random_digits_and_punctuation(N):  # Returns a string of N random digits/punctuation characters
    nonalpha = string.digits + string.punctuation
    return ''.join(secrets.choice(nonalpha) for n in range(0, N))


def random_digits(N):  # Returns a string of N random digits
    num = string.digits
    return ''.join(secrets.choice(num) for n in range(0, N))


def random_punctuation(N):  # Returns a string of N random punctuation characters
    special = string.punctuation    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    return ''.join(secrets.choice(special) for n in range(0, N))


def random_hex(N):  # Returns a string of N random hex characters (0-9, a-f, A-F)
    hexadec = string.hexdigits
    return ''.join(secrets.choice(hexadec) for n in range(0, N))


def random_safe_punctuation(N):  # Returns N random punctuation characters, excluding a blocklist of awkward ones (also prints the remaining set)
    special = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    lst = ['{', '}', "|", '[', ']', '/', '(', ')', '\\', '`', ',', '<', '<', '"', '\'']
    for x in lst:
        special = special.replace(x, '')
    print(special)
    return ''.join(secrets.choice(special) for n in range(0, N))