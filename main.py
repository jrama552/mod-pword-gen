from main_functions import *
from preset_vault import load_test_profiles
import time
import os

start = time.perf_counter()


# if file already exists, do nothing
if __name__ == '__main__':
    for file, init in init_list:
        if not os.path.exists(file):
            init()
run = True
while run:
    # need to mount list/files
    vault = []
    load_test_profiles(vault)
    print(f'vault: {vault}')
    run = run_menu_action(prompt_menu_choice(), vault)


end = time.perf_counter()
print(f'\n{end - start:.5f} seconds')


# LEFT OFF: ISSUE PASSWORD DOES NOT SAVE <----------------
# 2. adding profiles (acc, user, pword, tags), changing gen pwrd()
# 3. other center (search, remove, assign passwords to 'account')
# 4. save account/password pairs (password notepad) to file and retrieve
# 5. ask user for input (what do you want to generate w/ (i.e. the
# actual customization and modular part of the pword generation --> pword resets)
# 6. similar idea, but presents of generation