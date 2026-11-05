import json
import csv
import pykakasi     # pip install pykakasi
from gen_functions import *
from account_class import *
from input_functions import *


# --------------------------init files-----------------------------------


# loading file to list
def load_list_from_file(filename):  # loads a .json (returns the parsed list) or .csv (returns a list of rows), chosen by the filename
    if 'json' in filename:
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            return json.load(f)
    if 'csv' in filename:
        return read_csv_rows(filename)


def read_csv_rows(filename):  # reads csv file; returns a list of rows, each row a list of strings
    data = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for item in reader:
            data.append(item)
    # print(f'reading read_csv_rows data: \n{data}')
    return data


# writing list to file, returns nothing
def save_list_to_file(filename, list_data):  # writes a list to json or csv file, chosen by the filename; returns None
    if 'json' in filename:
        with open(filename, 'w') as f:
            json.dump(list_data, f, indent=4)
    if 'csv' in filename:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(list_data)


# cleaning of csv format, returns nothing
def clean_jp_csv(file='jp_file.csv'):  # reparses each row of the raw jp csv and writes the result to jp_dict.csv
    # initial 'cleaning'
    data = []
    with open(file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            item = row[0]
            item.strip('\"')    # unnecessary
            # csv.reader() acts a parser--(avoids , issues)
            item = next(csv.reader([item]))
            data.append(item)
        # print(data)

    # writing to new file
    save_list_to_file('jp_dict.csv', data)

# -----------------------------password gen functions -----------------------------------------


def build_password(order):  # builds a password from the ordered blocks, prints it, repeats until the user accepts; returns the final password string
    gen = True
    while gen:
        pword = ''
        for x in order:
            # sorting for functions; [[func, num], order]
            #                       x[0][0] x[0][1]  x[1]
            if len(x[0]) == 2:
                if callable(x[0][0]):
                    pword += x[0][0](x[0][1])
            else:
                pword += secrets.choice(load_list_from_file(x[0]))[0]
        print(f'Generated password:\n{pword}')
        gen = ask_regenerate()
    return pword


# LEFT OFF HERE: doesn't return to regeneration place

'''def profile_prompt():
    # list of current reading objects; make the below list an argument later
    vault = []  # vault is the list of 'profiles'
    valid = False
    new = ['n', 'new']
    reassign = ['re', 'reassign']
    print(f'ur in profile_prompt function')
    while not valid:
        decision = input('Generate password for [n]ew profile or [re]assign password to existing profile?')
        if decision.lower() in new:
            acc = input('Account/website name:\n')
            user = prompt_username()   # make an ever-extending list of usernames AND tags that user can add to at anytime
            tags = prompt_tags()   # tags should be a list; should also be accessing a list of pre-existing tabs
            new_profile = Profile(acc, user, '', tags)
            vault.append(new_profile)
            valid = True
        elif decision.lower() in reassign:

            # need to create a 'search' function first
            valid = True
            pass
        else:
            print("Respond with 'n' or 're'")'''


def choose_profile_index(vault):  # Prints a numbered list of profiles and asks the user to pick one; returns the chosen zero-based index
    # listing options
    # print(f'\x1B[3mFLAG:\x1B[0m you are viewing vault: {vault}')
    for num, item in enumerate(vault, start=1):
        print(f'{num}.', end='')
        item.print_profile()
    # identifying profile
    profile_index = int(input('Select profile:\n')) - 1
    # returning the index of the profile
    return profile_index


def assign_password_to_chosen(profile_lst, password):  # Lets the user pick a profile from the list and sets its password; returns False (ends the generate loop)
    selected_profile = profile_lst[choose_profile_index(profile_lst)]
    selected_profile.password = password
    print('Password saved.')
    return False


def filter_profiles(lst_tup, vault):  # Takes (query, field_key) and the vault; returns a list of Profiles whose chosen field contains the query
    #            (query, field, vault)
    query = lst_tup[0]
    field = lst_tup[-1]
    filtered = []
    for profile in vault:
        if field == 'a':
            if query in profile.acc:
                filtered.append(profile)
        elif field == 'u':
            if query in profile.user:
                filtered.append(profile)
        elif field == 'p':
            if query in profile.password:
                filtered.append(profile)
        else:
            if query in profile.tags:   # CHECK LATER (bc tags is a list)
                filtered.append(profile)
    return filtered


# ---------------------------------------------------------------------------------------------------------------------
def order_password_blocks(sources, characters):  # Determines the position of each password block (hard-coded while testing=True); returns the blocks sorted by position
    el_list = sources + characters  # list of [element, (number of char)]
    indexed_el = []     # list of [element, order/index]
    valid_range = [n for n in range(1, len(el_list) + 1)]
    print_password_blocks(el_list)
    testing = True  # true orders everything w/o manually asking everytime
    if testing:
        indexed_el = [[[random_hex, 2], 1], ['en_wordlist.json', 2],
                      [[random_digits, 2], 3], [[random_punctuation, 1], 3]]
    else:
        for el in el_list:
            # seperating elements (source or characters)
            if len(el) > 1:
                # validates user input and returns index order for each 'block/element'
                order = prompt_block_position(el, valid_range)
                indexed_el.append([[el[0], el[1]], order])
            else:
                order = prompt_block_position(el, valid_range)
                indexed_el.append([el[0], order])
            valid_range.remove(int(order))
    return sorted(indexed_el, key=lambda x: x[1])


def ask_save_password(word):  # Shows the password and asks whether to save it; returns True (yes) or False (no)
    print(f'Generated password: {word}')
    answer = False
    while not answer:
        save_input = input('Save this password?\n').lower()
        accept = ['yes', 'y']
        deny = ['no', 'n']
        if save_input in accept:
            answer = True
            return True
        elif save_input in deny:
            answer = True
            return False
        else:
            print('Respond with yes or no.\n')


def append_if_saved(value, word, lst):  # Appends word to lst if value is True and returns lst; otherwise returns None
    if value:
        lst.append(word)
        return lst


def print_saved_passwords(savelist):  # Prints each saved password, or "None" if the list is empty; returns None
    if not savelist:
        print(f'Passwords saved to file: None')
    else:
        print(f'Password(s) saved to file:')
        for x in savelist:
            print(x)

# function that translates and cuts words


def japanese_to_romaji_words(lst):  # Converts Japanese words to romaji and keeps only 6-letter results; returns a list of single-item lists
    kks = pykakasi.kakasi()
    romaji = []
    # start = time.perf_counter()
    for item in lst:
        roman = kks.convert(item)   # returns a list of dictionaries, hence [index][key]
        word = [roman[0]['hepburn']]    # listizing the words
        if 5 < len(word[0]) < 7:    # sorting
            romaji.append(word)
    return romaji
    # end = time.perf_counter()
    # print(f'{end - start:.5f} seconds') # so basically doesn't take a while luckily


# validates user input and returns order/index for each password element
def prompt_block_position(element, valid_range):  # Asks for a block's position until it's an int in valid_range; returns that int
    flag = False
    while not flag:
        if len(element) > 1:
            order = input(f'Order the block of custom characters from'
                          f' {char_dictionary[element[0].__name__]} within your password:\n')
            try:
                order = int(order)
            except ValueError:
                print('Try with an integer within the expected range.')
        else:
            order = input(f'Order the block of {element[0]} within your password:\n')
            try:
                order = int(order)
            except ValueError:
                print('Try with an integer within the expected range.')
        if order not in valid_range:
            print('Try with an integer within the expected range.')
        else:
            flag = True
            return order


# displays the blocks that will be included in the user's password
def print_password_blocks(lst):  # Prints the name/description of each block in the password; returns None
    # print('The following blocks will be included in your password:')
    for element in lst:
        if len(element) > 1:
            print(char_dictionary[element[0].__name__])
        else:
            print(element[0])

# --------------------------------------------------------------------------------------------------