from aux_functions import *
from gen_functions import *
from english_words import get_english_words_set     # pip install english-words


# ---------------------------init-------------------------------------------
def init_en():
    words = get_english_words_set(['web2'], lower=True)
    short_words = [[x] for x in words if 6 <= len(x) <= 8]
    write_file('en_wordlist.json', short_words)
    # print(read_file('en_wordlist.json'))


# cleans csv, extracts list, rewrites to clean csv
def init_jp():
    # clean csv
    clean_csv()
    # csv to list (extracting hirgana)
    jp = [row[1] for row in read_file('jp_dict.csv')]
    # translating
    romaji_jp = translator(jp)  # print(f'printing romaji list: \n{romaji_jp}')
    # writing file
    write_file('jp_wordlist.csv', romaji_jp)    # print(f' reading new wordlist: \n{read_file("jp_wordlist.csv")}')


init_list = [
    ['en_wordlist.json', init_en],
    #['jp_wordlist.csv', init_jp]
]


# pulling the lists to use
source_files = [[item[0]] for item in init_list]
# elements within password
char_list = [
    [gen_hexadec, 2],
    [gen_num, 2],
    [gen_punc, 1]
    # [gen_function, number of characters]
]
