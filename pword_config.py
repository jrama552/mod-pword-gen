from aux_functions import *
from gen_functions import *
from english_words import get_english_words_set     # pip install english-words


# ---------------------------init-------------------------------------------
def build_english_wordlist():  # Writes en_wordlist.json containing English words 6-8 letters long; returns None
    words = get_english_words_set(['web2'], lower=True)
    short_words = [[x] for x in words if 6 <= len(x) <= 8]
    write_file('en_wordlist.json', short_words)
    # print(read_file('en_wordlist.json'))


# cleans csv, extracts list, rewrites to clean csv
def build_japanese_wordlist():  # Cleans the raw JP csv, converts hiragana to romaji, writes jp_wordlist.csv; returns None
    # clean csv
    clean_jp_csv()
    # csv to list (extracting hirgana)
    jp = [row[1] for row in load_list_from_file('jp_dict.csv')]
    # translating
    romaji_jp = japanese_to_romaji_words(jp)  # print(f'printing romaji list: \n{romaji_jp}')
    # writing file
    save_list_to_file('jp_wordlist.csv', romaji_jp)    # print(f' reading new wordlist: \n{load_list_from_file("jp_wordlist.csv")}')


init_list = [
    ['en_wordlist.json', build_english_wordlist],
    #['jp_wordlist.csv', build_japanese_wordlist]
]


# pulling the lists to use
source_files = [[item[0]] for item in init_list]
# elements within password
char_list = [
    [random_hex, 2],
    [random_digits, 2],
    [random_safe_punctuation, 1]
    # [random_function, number of characters]
]