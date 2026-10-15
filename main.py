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

# 3. current: view ---> making 'view' function (in user functions vs in aux_functions)
# 4. save account/password pairs (password notepad) to file and retrieve
# 5. ask user for input (what do you want to generate w/ (i.e. the
# actual customization and modular part of the pword generation --> pword resets)
# 6. similar idea, but presents of generation

# main run config: if module, use 'main', not 'main.py' bc it looks for .py within main;
# if script, use main.py
