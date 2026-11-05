from pword_config import *


# gen pword and assign to new profile
def generate_and_assign_password(vault):  # gen a password, assigns to an existing profile (thru vie    w-all or filter); returns None
    generate = True
    while generate:
        word = build_password((order_password_blocks(source_files, char_list)))
        # reassign
        if ask_assign_to_existing():
            # view all --> assigning new password
            if ask_view_all():
                generate = assign_password_to_chosen(vault, word)
            # filter (search) --> assigning new password
                print(f'Objects after view and assigning password')
            for x in vault:
                x.print_profile()
            else:
                generate = assign_password_to_chosen(filter_profiles(prompt_search_criteria(), vault), word)
                print(f'Objects after filtering and assigning password')
        # creating new profile
        else:
            pass    # use profile_prompt

        '''vault = append_if_saved(ask_save_password(word), word, vault)
        generate = ask_regenerate()'''