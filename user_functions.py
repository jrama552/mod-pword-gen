from pword_config import *


# gen pword and assign to new profile
def generate_password(vault):
    generate = True
    while generate:
        word = gen_pword((order_el(source_files, char_list)))
        # reassign
        if user_reassign(): # find existing profile
            # view all --> assigning new password
            if user_view():
                generate = view_assign(vault, word, False)
            # filter (search) --> assigning new password
                # print(f'Objects after view and assigning password')
            else:
                print(f'line 17')
                generate = view_assign(filter_search(filter_vault(), vault), word, False) # left off in filter_vault
                # print(f'Objects after filtering and assigning password')
            for x in vault:
                x.printo()
        # creating new profile
        else: # create new profile
            generate = view_assign(profile_prompt(vault), word, True)   # use profile_prompt

        '''vault = save_word(save_prompt(word), word, vault)
        generate = gen_prompt()'''

        '''def view_profile(vault):
            # lwk just call view()
            for x in vault:
                print(f' this is yo vault: {x.printo()}')'''


