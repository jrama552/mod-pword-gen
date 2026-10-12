

def user_reassign():
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


def gen_prompt():
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
            print('Answer with re/u')
            flag = True


def user_view():
    view_str = ['v', 'view']
    filter_str = ['f', 'filter']

    answer = False
    while not answer:
        field = input('[v]iew all or [f]ilter profiles?\n')
        # VIEW
        if field.lower() in view_str:
            answer = True
            return True
        elif field.lower() in filter_str:
            answer = True
            return False
        else:
            print('Please choose one of the above options')


def filter_vault():
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
            if field.lower() == 't':
                tags = []
                tag_query = input(f'Search {field_filter[field]}(separate tags with a comma and space):\n')
                for tag in tag_query.split(', '):
                    print(f'you\'ve reached tag.split() of input; this is tag: {tag}')
                    tags.append(tag.lower())
                    print(f'Tags: {tags}')
                    field_flag = False
                return tags, field.lower()
            else:
                field_flag = False
                return [input(f'Search {field_filter[field]}:\n').lower()], field
                # query, field
        else:
            print(f'Please enter one of the options above.')
            field_flag = True



def get_user():     # most likely a list of pre-existing users
    return input('Username:\n')


def get_tags():     # most likely a list of pre-existing tags
    tags = input('Account tags: \n').split(', ')
    print(tags)
    return tags






