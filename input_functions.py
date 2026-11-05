def ask_assign_to_existing():  # Asks existing vs. new profile; returns True (existing), False (new), or None on invalid input
    exist_str = ['e', 'existing']
    new_str = ['n', 'new']
    field = input('Do assign password to [e]xisting profile or [n]ew profile?\n')
    # VIEW
    if field.lower() in exist_str:
        return True
    elif field.lower() in new_str:
        return False
    else:
        print('Please choose one of the above options')


def ask_regenerate():  # asks use vs. regenerate until valid; returns True to regenerate, False to use the password
    flag = True
    while flag:
        re = ['regenerate', 're']
        use = ['u', 'use']
        decision = input('[u]se password or [re]generate?\n')
        if decision.lower() in use:
            flag = False
            return False
        elif decision.lower() in re:
            flag = False
            return True
        else:
            print('Answer with y/n')
            flag = True


def ask_view_all():  # Asks view-all vs. filter; returns True for view all, False for filter
    view_str = ['v', 'view']
    filter_str = ['f', 'filter']
    field = input('[v]iew all or [f]ilter profiles?\n')
    answer = False
    while not answer:
        # VIEW
        if field.lower() in view_str:
            answer = True
            return True
        elif field.lower() in filter_str:
            answer = True
            return False
        else:
            print('Please choose one of the above options')


def prompt_search_criteria():  # Asks which field to search and the search text; returns a tuple (query, field_key), e.g. ('git', 'a')
    field_filter = {
        'a': 'account',
        'u': 'user',
        'p': 'password',
        't': 'tags'
    }
    field_flag = True
    while field_flag:
        field = input('What field do you wish to filter through?\n[a]ccount, [u]sername, [p]assword, [t]ags\n')
        if field.lower() in field_filter.keys():
            field_flag = False
        else:
            print(f'Please enter one of the options above.')
            field_flag = True
    return input(f'Search {field_filter[field]}:\n'), field


# most likely a list of pre-existing users
def prompt_username():  # Prompts for a username; returns the entered string
    return input('Username:\n')


# most likely a list of pre-existing tags
def prompt_tags():  # Prompts for one tag; returns it inside a list
    tags = [input('Account tags')]
    return tags