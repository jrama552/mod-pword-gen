from main_functions import *
from preset_vault import preset_vault
import time
import os

start = time.perf_counter()


# if file already exists, do nothing
if __name__ == '__main__':
    for file, init in init_list:
        if not os.path.exists(file):
            init()
vault = []
preset_vault(vault)
run = True
while run:
    # need to mount list/files
    print(f'vault: {vault}')
    run = direct_user(user_action(), vault)


end = time.perf_counter()
print(f'\n{end - start:.5f} seconds')


# view function finished (need to do more testing late though)
# 4. save account/password pairs (password notepad) to file and retrieve (keep storage medium uniform (json/csv)
# 5. ask user for input (what do you want to generate w/ (i.e. the
# actual customization and modular part of the pword generation --> pword resets)
# 6. similar idea, but presents of generation

# not sure if addressed: # 3. need to fix profile.lowered() function, tags splitter, and
